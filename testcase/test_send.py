import yaml


def test_send():

    env = {
        "docker.testing-studio.com": {
            "dev": "127.0.0.1",
            "test": "1.1.1.2"
        },
        "default": "dev"
    }
    yaml2 = yaml.safe_dump(env)
    print("")
    print(yaml2)

