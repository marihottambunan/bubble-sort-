def bubble_sort_with_input():
    print("=== Program Bubble Sort dengan Input ===")
    
    # Meminta input array dari pengguna
    input_str = input("Masukkan elemen array (pisahkan dengan spasi): ")
    arr = list(map(int, input_str.split()))
    
    print(f"\nArray awal: {arr}")
    n = len(arr)
    
    for i in range(n):
        print(f"\nPass {i+1}:")
        swapped = False
        
        for j in range(n-i-1):
            print(f"  Bandingkan {arr[j]} dan {arr[j+1]}", end='')
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(" -> swap")
            else:
                print(" -> tetap")
            
            print(f"  Array sekarang: {arr}")
        
        # Optimasi: berhenti jika tidak ada swap
        if not swapped:
            print("\nTidak ada swap pada pass ini, array sudah terurut!")
            break
    
    print(f"\nHasil akhir: {arr}")

if __name__ == "__main__":
    bubble_sort_with_input()