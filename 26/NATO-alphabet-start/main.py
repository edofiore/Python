import pandas as pd



def main() -> None:
    
    # read cv
    
    alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
    
    # print cv
    #print(alphabet_df.head())
    # request word
    
    dc = {
        row["letter"] : row["code"] for index,row in alphabet_df.iterrows()
    }
    print(dc)
    
    input_word = input("Insert the word to spell: ")
    
    
    result_list = [ dc[letter] for letter in input_word.upper()]
    
    print(result_list)
    

    

if __name__ == "__main__":
    
    print("IN")
    main()
    