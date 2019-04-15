from numpy import fft

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    ans = fft.fft(arr)

    for i in ans:
        print(i)

main()