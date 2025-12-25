"""
HNP Router
Fractal hierarchical routing with O(log_φ n) complexity
"""

import math
from typing import List, Tuple, Optional


class FractalNode:
    """Node in fractal routing tree"""
    
    def __init__(self, address: int, level: int, parent: Optional['FractalNode'] = None):
        self.address = address
        self.level = level
        self.parent = parent
        self.children: List['FractalNode'] = []
    
    def add_child(self, child: 'FractalNode'):
        """Add child node"""
        self.children.append(child)
        child.parent = self
    
    def get_path_to_root(self) -> List['FractalNode']:
        """Get path from this node to root"""
        path = [self]
        current = self
        while current.parent:
            current = current.parent
            path.append(current)
        return path
    
    def __repr__(self) -> str:
        return f"FractalNode(addr=0x{self.address:08X}, level={self.level})"


class HNPRouter:
    """
    Harmonic Network Router with fractal addressing
    
    31-bit hierarchical address space:
    - Level 1: 2 bits (quadrants)
    - Level 2: 3 bits (octants)
    - Level 3: 5 bits (φ-subdivision)
    - Level 4: 8 bits (Fibonacci)
    - Level 5: 13 bits (Fibonacci continuation)
    Total: 31 bits (Mersenne prime!)
    """
    
    PHI = 1.618033988749895
    LEVEL_BITS = [2, 3, 5, 8, 13]  # Fibonacci-like progression
    
    def __init__(self):
        """Initialize router with fractal tree"""
        self.root = FractalNode(address=0, level=0)
        self.address_map = {0: self.root}
        self._build_initial_tree()
    
    def _build_initial_tree(self):
        """Build initial fractal tree structure"""
        # This would be populated dynamically in real implementation
        # For now, create a simple structure
        pass
    
    def register_node(self, address: int) -> bool:
        """
        Register a new node in the fractal tree
        
        Args:
            address: 31-bit address to register
        
        Returns:
            bool: Success
        """
        if address in self.address_map:
            return False
        
        # Find appropriate parent based on prefix matching
        level, parent = self._find_parent(address)
        
        # Create node
        node = FractalNode(address=address, level=level, parent=parent)
        
        if parent:
            parent.add_child(node)
        
        self.address_map[address] = node
        return True
    
    def _find_parent(self, address: int) -> Tuple[int, Optional[FractalNode]]:
        """
        Find appropriate parent node for address
        
        Returns:
            tuple: (level, parent_node)
        """
        # Extract level information from address
        level = 1
        cumulative_bits = 0
        
        for level_bits in self.LEVEL_BITS:
            cumulative_bits += level_bits
            
            # Check if we have a parent at this level
            parent_addr = address & ((1 << cumulative_bits) - 1)
            parent_addr = parent_addr & ~((1 << level_bits) - 1)  # Clear last level
            
            if parent_addr in self.address_map:
                return (level, self.address_map[parent_addr])
            
            level += 1
        
        # No specific parent found, use root
        return (1, self.root)
    
    def route(self, src: int, dst: int) -> List[int]:
        """
        Find route from source to destination
        
        Args:
            src: Source address (31-bit)
            dst: Destination address (31-bit)
        
        Returns:
            list: Path of addresses (including src and dst)
        """
        # Get nodes
        src_node = self.address_map.get(src)
        dst_node = self.address_map.get(dst)
        
        if not src_node or not dst_node:
            # Node not registered, do best effort
            return self._route_unregistered(src, dst)
        
        # Find lowest common ancestor
        src_path = src_node.get_path_to_root()
        dst_path = dst_node.get_path_to_root()
        
        # Find LCA
        lca = self._find_lca(src_path, dst_path)
        
        # Build path: src -> lca -> dst
        path_up = self._path_to_ancestor(src_node, lca)
        path_down = self._path_from_ancestor(lca, dst_node)
        
        # Combine (remove duplicate LCA)
        full_path = path_up + path_down[1:]
        
        return [node.address for node in full_path]
    
    def _find_lca(self, path1: List[FractalNode], path2: List[FractalNode]) -> FractalNode:
        """Find lowest common ancestor"""
        # Reverse paths (root first)
        path1 = list(reversed(path1))
        path2 = list(reversed(path2))
        
        lca = path1[0]  # Root
        
        for n1, n2 in zip(path1, path2):
            if n1.address == n2.address:
                lca = n1
            else:
                break
        
        return lca
    
    def _path_to_ancestor(self, node: FractalNode, ancestor: FractalNode) -> List[FractalNode]:
        """Get path from node to ancestor"""
        path = [node]
        current = node
        
        while current.address != ancestor.address and current.parent:
            current = current.parent
            path.append(current)
        
        return path
    
    def _path_from_ancestor(self, ancestor: FractalNode, node: FractalNode) -> List[FractalNode]:
        """Get path from ancestor to node"""
        path = self._path_to_ancestor(node, ancestor)
        return list(reversed(path))
    
    def _route_unregistered(self, src: int, dst: int) -> List[int]:
        """
        Route between unregistered nodes
        Use XOR distance as heuristic
        """
        # Simple direct route for unregistered
        return [src, dst]
    
    def distance(self, src: int, dst: int) -> int:
        """
        Calculate harmonic distance between addresses
        
        Distance = number of levels to traverse
        """
        path = self.route(src, dst)
        return len(path) - 1
    
    def get_neighbors(self, address: int, max_distance: int = 1) -> List[int]:
        """
        Get neighboring addresses within max_distance
        
        Args:
            address: Center address
            max_distance: Maximum harmonic distance
        
        Returns:
            list: Neighbor addresses
        """
        neighbors = []
        
        node = self.address_map.get(address)
        if not node:
            return neighbors
        
        # BFS up to max_distance
        visited = {address}
        queue = [(node, 0)]
        
        while queue:
            current, dist = queue.pop(0)
            
            if dist < max_distance:
                # Add children
                for child in current.children:
                    if child.address not in visited:
                        neighbors.append(child.address)
                        visited.add(child.address)
                        queue.append((child, dist + 1))
                
                # Add parent
                if current.parent and current.parent.address not in visited:
                    neighbors.append(current.parent.address)
                    visited.add(current.parent.address)
                    queue.append((current.parent, dist + 1))
        
        return neighbors
    
    def optimize_topology(self):
        """
        Optimize fractal tree topology based on traffic patterns
        In real implementation, this would reorganize nodes for minimal distance
        """
        # Placeholder for optimization algorithm
        pass
    
    def get_statistics(self) -> dict:
        """Get routing statistics"""
        total_nodes = len(self.address_map)
        
        # Calculate tree depth
        max_depth = 0
        for node in self.address_map.values():
            path_len = len(node.get_path_to_root())
            max_depth = max(max_depth, path_len)
        
        return {
            'total_nodes': total_nodes,
            'max_depth': max_depth,
            'theoretical_depth': math.ceil(math.log(total_nodes, self.PHI)) if total_nodes > 1 else 0,
            'efficiency': max_depth / math.ceil(math.log(total_nodes, self.PHI)) if total_nodes > 1 else 1.0,
        }
    
    def __repr__(self) -> str:
        stats = self.get_statistics()
        return (
            f"HNPRouter("
            f"nodes={stats['total_nodes']}, "
            f"depth={stats['max_depth']}, "
            f"efficiency={stats['efficiency']:.2f})"
        )
