import sys
import argparse

from mnist_app.api import run


def _parse_cmd_args(*args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-p",
                        "--port",
                        help="Port number for the APP (default: 5000)",
                        required=False,
                        default=None)
    parser.add_argument("-d",
                        "--device",
                        help="Device: 'CPU', 'CUDA'... (default: 'CPU')",
                        required=False,
                        default=None)
    parser.add_argument("-c",
                        "--config-path",
                        help="Path to a config file in yaml format",
                        required=False,
                        default=None)
    
    cmd_args = parser.parse_args(args)
    return cmd_args.__dict__


if __name__ == "__main__":
    args_dict = _parse_cmd_args(*sys.argv[1:])
    run(**args_dict)

