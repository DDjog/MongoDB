import connect
import models
import seeds

if __name__ == '__main__':

    seeds.delete_data()
    seeds.put_data_to_mongo()

    while True:
        instr = input(">")

        if instr == "exit":
            break

        strlist = instr.split(":")

        if strlist[0] == "name":
            # print( "author name:", strlist[1].strip() )
            # author_fullname = "Albert Einstein"
            author_fullname = strlist[1].strip()
            # print("Author:")
            quote_by_author = models.find_quote_by_author(author_fullname)
            if quote_by_author is not None:
                for q in quote_by_author:
                    print(q.quote)
                    print(q.author.fullname)
                    print()
            else:
                print("No such an author ", author_fullname)

        if strlist[0] == "tag":
            # print( "tag name:", strlist[1].strip() )
            # print("Quote by single tag:\n")
            # tag = "life"
            tag = strlist[1].strip()
            single_tag = models.find_single_tag(tag)
            if single_tag is not None:
                for q in single_tag:
                    print(q.quote)
                    print(q.author.fullname)
                    print()
            else:
                print("No defined tag")

        if strlist[0] == "tags":
            tagsstr = strlist[1].strip()
            tagslist = tagsstr.split(",")
            print("tags:", len(tagslist))
            tags = []
            for t in tagslist:
                tags.append(t)
            # print(arraytag)
            # print("Quote by multile tag:\n")
            # tags = ["success"]
            tags = models.find_tags(tags)
            if tags is not None:
                for q in tags:
                    print(q.quote)
                    print(q.author.fullname)
                    print()
            else:
                print("No tags")
