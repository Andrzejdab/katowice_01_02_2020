statuses = {
    "Alice": "online",
    "Rafał" : "ofline",
    "Anna": "online"
}

def status_count(statuses,status):
    # k =0
    # for i, status in statuses.items() :
    #     if stat == status:
    #         k += 1
    # return k
    return lista(statuses.values()).count(status)


def test_status_count_with_existing_status():
    statuses = {
        "Alice": "online",
        "Rafał": "ofline",
        "Anna": "online"

    }
    assert status_count(statuses, "online")  == 2