import requests
import json

# يطلب منك اسم الـ subreddit وعدد المنشورات
subreddit = input("Enter subreddit name: ")
limit = int(input("Enter number of posts: "))

# رابط واجهة Reddit العامة
url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
headers = {"User-Agent": "Dalal-YARS/0.1"}

# نجلب البيانات من Reddit
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"❌ Error: {response.status_code} – make sure the subreddit exists or try later.")
else:
    data = response.json()

    posts = []
    for post in data["data"]["children"]:
        item = post["data"]
        posts.append({
            "title": item["title"],
            "author": item["author"],
            "score": item["score"],
            "url": item["url"]
        })

    # الاسم الديناميكي للملف
    filename = f"{subreddit}_data.json"

    # نحفظ النتائج في ملف JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Saved {len(posts)} posts to {filename}")

    # عرض أول 3 منشورات من النتيجة
    print("\n📋 أول 3 منشورات:")
    for i, post in enumerate(posts[:3], 1):
        print(f"{i}. {post['title']} — by {post['author']} (👍 {post['score']})")