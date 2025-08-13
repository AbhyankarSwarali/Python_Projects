# Mad Libs Story Generator  

This Python program lets you create interactive Mad Libs stories. It reads a text file containing a story template with placeholders (wrapped in `< >`), asks the user for words to fill in those placeholders, and then outputs a completed story.  

## How It Works  
1. Load a story from **`Story.txt`**.  
2. Detect all unique placeholders in the format `<placeholder>`.  
3. Prompt the user to provide words for each placeholder.  
4. Replace all placeholders in the story with the provided words.  
5. Display the completed, customized story.  

## Key Logic Snippet  
```python
words = set()
start_of_word = -1

for i, char in enumerate(story):
    if char == '<':
        start_of_word = i
    if char == '>' and start_of_word != -1:
        word = story[start_of_word : i+1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words: 
    answers[word] = input("Enter a word for " + word + ': ')

for word in words:
    story = story.replace(word, answers[word])
```

## Example  
If **Story.txt** contains:  
```
Once upon a time, there was a <adjective> <noun> who loved to <verb>.
```  
You might see:  
```
Enter a word for <adjective>: funny  
Enter a word for <noun>: cat  
Enter a word for <verb>: dance  
```  
Final story:  
```
Once upon a time, there was a funny cat who loved to dance.
```  

## Requirements  
- Python 3.x  
- **Story.txt** in the same folder as the script  

## Run the Program  
```bash
python your_script_name.py
```

## Awaken the storyteller within you ;)
