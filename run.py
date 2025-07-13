#!/usr/bin/env python3
"""
Main entry point for the LinkLine application.
Run different components based on command line arguments.
"""

import sys
import argparse
from app import app
from app.voice_agent.api import app as voice_app

def main():
    parser = argparse.ArgumentParser(description='LinkLine Application')
    parser.add_argument('--component', choices=['main', 'voice'], 
                       default='main', help='Which component to run')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    if args.component == 'voice':
        print(f"Starting Voice Agent API on {args.host}:{args.port}")
        voice_app.run(host=args.host, port=args.port, debug=args.debug)
    else:
        print(f"Starting Main Application on {args.host}:{args.port}")
        app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()
