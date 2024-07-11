def designerPdfViewer(h, word):
    maxx = 0
    
    for ch in word:
        num = ord(ch) - ord('a')
        if h[num] > maxx:
            maxx = h[num]
    
    return maxx * 1 * len(word)


res = designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], "abc")
print(f"res -> {res}")