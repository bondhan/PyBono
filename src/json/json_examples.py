import json
from pprint import pprint


def example_json_processing():
    data_1 = "this is a string"
    data_2 = 1234
    data_3 = 1.234

    plain = "{\n" \
            + "	\"data_1\": \"" + data_1 + "\",\n" \
            + "	\"data_2\": \"" + str(data_2) + "\",\n" \
            + "	\"data_3\": \"" + str(data_3) + "\"\n" \
            + "}";

    # in memory
    # plain =
    #
    #     '{
    #     "data_1": "this is a string",
    #     "data_2": "1234",
    #     "data_3": "1.234"
    #
    # }'

    print(f"plain = {plain}")

    loaded = json.loads(plain)
    # loads will remove the whitespaces and replace " to '
    # loaded = {'data_1': 'this is a string', 'data_2': '1234', 'data_3': '1.234'}

    print(f"loaded = {loaded}")

    json_obj = json.dumps(loaded)
    # convert to json
    # dumped = '{"data_1": "this is a string", "data_2": "1234", "data_3": "1.234"}'

    print(f"dumped = {json_obj}")

    print("This is what happpened if we convert directly to json")
    c = json.dumps(plain)
    print(f"c = {c}")

    return json_obj


if __name__ == '__main__':
    json_obj = example_json_processing()

