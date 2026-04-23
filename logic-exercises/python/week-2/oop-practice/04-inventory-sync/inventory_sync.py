def get_sync(list_1, list_2):
    non_repeated = []

    for i in list_1:
        if not i in list_2:
                non_repeated.append(i)

    return non_repeated


if __name__ == "__main__":
    server_list_1 = ["python", "git", "docker", "nginx"]
    server_list_2 = ["git", "nginx", "bash"]

    tech = get_sync(server_list_1, server_list_2)
    print(tech)