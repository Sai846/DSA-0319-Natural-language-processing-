import re
def main():
    text = input("Enter some text: ")
    pattern = r'\b[Aa]\w+'
    matches = re.findall(pattern, text)
    print("Words starting with 'A' or 'a':")
    for match in matches:
        print(match)
if __name__ == "__main__":
    main()
import re 
text="new dog1233"
word=r'\bdog[0-9]*\b'
match1=re.findall(word,text)
if match1:
  print("match found")
  for a in match1:
    print(a)
else:
    print("no match found")
