import requests
from os import system
from sys import platform


def download_for_linux(image_link):  # For linux machine
    system(f"wget -nv {image_link}")


def main(link, no_of_pages):

    part1 = "https://danbooru.donmai.us/posts?page="
    page = 1  # part2 is page
    part3 = "&tags="
    part4 = link.split("tags=")[-1]

    while page <= no_of_pages:
        link = f"{part1}{page}{part3}{part4}"
        print(f"current page is :: {link}")

        res = requests.get(link)
        with open("index.txt", "w+", encoding="utf-8") as fh:
            fh.write(res.text)

        count_of_images_on_this_page = 0
        list_of_links = []
        fh = open("index.txt", "r", encoding="utf-8")
        for line in fh:
            for word in line.strip().split():
                if 'data-file-url="https://cdn.donmai.us/original' in word:
                    final_link_of_image = word.split("data-file-url=")[1][1:-1]
                    list_of_links.append(final_link_of_image)
                    download_for_linux(final_link_of_image)
                    count_of_images_on_this_page += 1

        if count_of_images_on_this_page == 0:
            return

        # print(*list_of_links, sep="\n", end="\n\n")
        print("DONE", count_of_images_on_this_page)

        page += 1


if __name__ == "__main__":

    link = input("Enter the link :: ")
    if link == "":
        link = "https://danbooru.donmai.us/posts?tags=ganyu_%28genshin_impact%29"
    try:
        no_of_pages = int(input("Enter the no of pages :: "))
    except:
        no_of_pages = 1

    main(link, no_of_pages)
