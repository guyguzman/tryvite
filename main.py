import json
import time

def print_children(children, indent=0):
    """Recursively prints information about each child."""
    try:
        for child in children:
            # Print child keys or a specific field, e.g., 'name'
            name = child.get("name", "No Name")
            print(" " * indent + f"- {name}")
            
            # If there are nested children, recursively print them
            if "children" in child:
                print_children(child["children"], indent + 2)
    except Exception as e:
        print("Error:", e)

def main():
    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(type(my_dict))
 
    local_time = time.localtime()

    # Format the local time as a readable string
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print("Formatted Local Time:", formatted_time)

    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

    # Load the JSON from a local file
    bookmarks_file = r"C:\Users\guygu\AppData\Local\Microsoft\Edge\User Data\Default\bookmarks"
    local_bookmarks_file = "originalBookmarks.json"

    with open(bookmarks_file, "r", encoding="utf-8",errors="replace") as f:
        data = json.load(f)
    
    print(type(data))
    print("Made it this far")   

    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Division by zero error.")
    else:
        print("No exceptions encountered. The result is:", result)

    url_list = []

    for key in data.keys():
        if(key == "roots"):
            roots = data["roots"]
            for keyRoots in roots.keys():
                if(keyRoots == "bookmark_bar"):
                    bookmark_bar = roots["bookmark_bar"]
                    for keyBookmarkBar in bookmark_bar.keys():
                        if(keyBookmarkBar == "children"):
                            bookmarkBarChildren = bookmark_bar["children"]
                            for child in bookmarkBarChildren:
                                if(child["name"] == "Personal"):
                                    personalList = child
                                    for personalChild in personalList["children"]:
                                        if(personalChild["name"]) == "AI":
                                            aiList = personalChild
                                            json_hierarchy_string = json.dumps(aiList.get('children', []), indent=2)
                                            with open('ai_bookmarks.json', 'w') as file:
                                                file.write(json_hierarchy_string)
                                            # print(json_hierarchy_string)
                                            # for aiChild in aiList["children"]:
                                            #     variable_type = aiChild.get('type', 'No Type')
                                            #     is_Array = isinstance(aiChild.get('children', []), list)
                                            #     children_Count = len(aiChild.get('children', []))
                                            #     if(variable_type == "url"):
                                            #         url_list.append(aiChild["url"])
                                            #         print(f"{aiChild['name']} - {aiChild['url']} - {variable_type}")
                                            #     if(variable_type == "folder"):
                                            #         print(f"{aiChild['name']} - Count: {children_Count} - {variable_type}")
                                            #         for folderChildren in aiChild["children"]:
                                            #             print(f"  - {folderChildren['name']} - {folderChildren['url']} - {folderChildren.get('type', 'No Type')}")  
                                            
                                    # print(url_list)
                                    with open('bookmarks.txt', 'w') as file:
                                        for url in url_list:
                                            file.write(f"{url}\n")
                            

                
    # If your JSON has "children" as a top-level key
    if "rootsX" in data:
        print("Top-level children:")
        print_children(data["roots"].get("bookmark_bar", {}).get("children", []))

    else:
        print("No top-level 'children' key found. Adjust the code as needed.")

if __name__ == "__main__":
    main()
