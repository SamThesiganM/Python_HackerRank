def solve(s):
    st=s
    words=s.split()
    for word in words:
        new_word=word[0].strip().upper()+word[1:]
        st=st.replace(word,new_word) 
    return st
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()