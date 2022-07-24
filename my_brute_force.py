def my_brute_force(arr, key):
    arr_ptr = 0
    key_ptr = 0
    while key_ptr != len(key):  # 찾거나
        if key_ptr == 0 and arr_ptr - key_ptr > len(arr) - arr_ptr:  # 관찰할 arr_ptr의 개수보다 len(key)가 더커서 서치가 무의미할때
            break
        if arr[arr_ptr] == key[key_ptr]:
            arr_ptr += 1
            key_ptr += 1
        else:
            arr_ptr = arr_ptr - key_ptr + 1
            key_ptr = 0
    if key_ptr == len(key):
        return ("find it")
    else:
        return ("search failed")


if __name__ == "__main__":
    arr = list(input())
    key = input()
    print(my_brute_force(arr, key))
