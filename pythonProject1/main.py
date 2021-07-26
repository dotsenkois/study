def print_rangoli(size):
    # your code goes here

    alfabet = 'abcdefghijklmopqrstuvwxyz'
    for i in range(size):
        temp= alfabet[size-26-i:size]+ '_'*(size-1-i)
        print(temp)
        temp_sum= temp[::-1] + temp[1:]
        print(temp_sum)

    # for i in range(size):
    #     temp_str= alfabet[size-1-i:size]
    #     print(f"temp str {temp_str}")
    #     for j in range(len(temp_str)):
    #
    #
    #         print(temp_str[-j])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)