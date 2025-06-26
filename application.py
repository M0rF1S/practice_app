import argparse
from form_matcher import find_matching_template

def analyze_values():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["get_tpl"])
    parser.add_argument("--params", nargs="*", help="Field=value pairs")
    return parser.parse_args()

def main():
    args = analyze_values()
    if args.command == "get_tpl" and args.params:
        input_data = dict(param.split("=") for param in args.params)
        result = find_matching_template("database.json", input_data)

        if isinstance(result, str):
            print(result)
        else:
            print("{")
            for k, v in result.items():
                print(f"  {k}: {v},")
            print("}")

if __name__ == "__main__":
    main()