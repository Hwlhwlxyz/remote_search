from src.remote_search import remote_search
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='search files on servers')
    parser.add_argument('input', metavar='S', type=str,
                        help='an string to search')
    args = parser.parse_args()
    print("input:", args.input)
    con_list = remote_search.run(args.input)
    for c in con_list:
        print(c.get_name())
        print(c.get_result())