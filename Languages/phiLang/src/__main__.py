#!/usr/bin/env python3
"""
ΦLang Command Line Interface

Usage:
    philang compile <file.phi> [-o output.phic]
    philang run <file.phic>
    philang decompile <file.phic> [-o output.phi]
    philang validate <file.phi>
    philang --version
    philang --help
"""

import sys
import argparse
from pathlib import Path

from .compiler.parser import Parser
from .compiler.validator import Validator
from .compiler.encoder import Encoder
from .compiler.decoder import Decoder
from .runtime.executor import Executor


__version__ = "1.0.0"


def compile_file(input_path: str, output_path: str = None):
    """Compile .phi file to .phic bytecode"""
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        return 1
    
    # Read source
    source = input_file.read_text()
    
    # Parse
    print(f"Parsing {input_path}...")
    parser = Parser()
    try:
        ast = parser.parse(source)
    except Exception as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return 1
    
    # Validate
    print(f"Validating...")
    validator = Validator()
    try:
        validator.validate(ast)
    except Exception as e:
        print(f"Validation error: {e}", file=sys.stderr)
        return 1
    
    # Encode
    print(f"Encoding to bytecode...")
    encoder = Encoder()
    try:
        bytecode = encoder.encode(ast)
    except Exception as e:
        print(f"Encoding error: {e}", file=sys.stderr)
        return 1
    
    # Write output
    if output_path is None:
        output_path = input_file.with_suffix('.phic')
    
    output_file = Path(output_path)
    output_file.write_bytes(bytecode)
    
    print(f"✓ Compiled successfully: {output_path}")
    print(f"  Instructions: {len(ast)}")
    print(f"  Bytecode size: {len(bytecode)} bytes")
    
    return 0


def run_file(bytecode_path: str):
    """Execute .phic bytecode"""
    bytecode_file = Path(bytecode_path)
    
    if not bytecode_file.exists():
        print(f"Error: File not found: {bytecode_path}", file=sys.stderr)
        return 1
    
    # Read bytecode
    bytecode = bytecode_file.read_bytes()
    
    # Execute
    print(f"Executing {bytecode_path}...")
    executor = Executor()
    try:
        result = executor.execute(bytecode)
        print(f"✓ Execution completed")
        print(f"  Result: {result}")
    except Exception as e:
        print(f"Execution error: {e}", file=sys.stderr)
        return 1
    
    return 0


def decompile_file(bytecode_path: str, output_path: str = None):
    """Decompile .phic bytecode to .phi source"""
    bytecode_file = Path(bytecode_path)
    
    if not bytecode_file.exists():
        print(f"Error: File not found: {bytecode_path}", file=sys.stderr)
        return 1
    
    # Read bytecode
    bytecode = bytecode_file.read_bytes()
    
    # Decode
    print(f"Decompiling {bytecode_path}...")
    decoder = Decoder()
    try:
        ast = decoder.decode(bytecode)
    except Exception as e:
        print(f"Decoding error: {e}", file=sys.stderr)
        return 1
    
    # Generate source
    source = decoder.ast_to_source(ast)
    
    # Write output
    if output_path is None:
        output_path = bytecode_file.with_suffix('.phi')
    
    output_file = Path(output_path)
    output_file.write_text(source)
    
    print(f"✓ Decompiled successfully: {output_path}")
    print(f"  Instructions: {len(ast)}")
    
    return 0


def validate_file(input_path: str):
    """Validate .phi file syntax and semantics"""
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        return 1
    
    # Read source
    source = input_file.read_text()
    
    # Parse
    print(f"Parsing {input_path}...")
    parser = Parser()
    try:
        ast = parser.parse(source)
    except Exception as e:
        print(f"✗ Parse error: {e}", file=sys.stderr)
        return 1
    
    # Validate
    print(f"Validating...")
    validator = Validator()
    try:
        validator.validate(ast)
    except Exception as e:
        print(f"✗ Validation error: {e}", file=sys.stderr)
        return 1
    
    print(f"✓ File is valid")
    print(f"  Instructions: {len(ast)}")
    
    return 0


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="ΦLang - Mathematical Programming Language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  philang compile hello.phi
  philang compile hello.phi -o hello.phic
  philang run hello.phic
  philang decompile hello.phic
  philang validate hello.phi

For more information: https://github.com/quantum-lichen/philang
        """
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'ΦLang {__version__}'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Compile command
    compile_parser = subparsers.add_parser(
        'compile',
        help='Compile .phi source to .phic bytecode'
    )
    compile_parser.add_argument('input', help='Input .phi file')
    compile_parser.add_argument('-o', '--output', help='Output .phic file')
    
    # Run command
    run_parser = subparsers.add_parser(
        'run',
        help='Execute .phic bytecode'
    )
    run_parser.add_argument('input', help='Input .phic file')
    
    # Decompile command
    decompile_parser = subparsers.add_parser(
        'decompile',
        help='Decompile .phic bytecode to .phi source'
    )
    decompile_parser.add_argument('input', help='Input .phic file')
    decompile_parser.add_argument('-o', '--output', help='Output .phi file')
    
    # Validate command
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate .phi file'
    )
    validate_parser.add_argument('input', help='Input .phi file')
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 0
    
    # Execute command
    if args.command == 'compile':
        return compile_file(args.input, args.output)
    elif args.command == 'run':
        return run_file(args.input)
    elif args.command == 'decompile':
        return decompile_file(args.input, args.output)
    elif args.command == 'validate':
        return validate_file(args.input)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
