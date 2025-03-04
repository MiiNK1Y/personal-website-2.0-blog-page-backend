# Aleksander's Blog API
Made independent from the static 'portfolio' front-end served on [alnyk.pages.dev](https://alnyk.pages.dev).
It returns either;
- A JSON array with metadata for each blogpost.
- HTML markup for a single post.

---
# Usage
---
Endpoint: **https://alnyk.net/blog/all_posts**

Results in the following response:
```json
[
  {
    "date-of-last-edit": "16.02.2025",
    "date-of-posting": "16.02.2025",
    "description": "In this description, we write what the blog post is about, like an intro, or maybe a TL;DR.",
    "post-url": "post-two",
    "preview-img-url": "/images/post_two.webp",
    "tags": "#here, #we, #store, #tags",
    "title": "Post two"
  },
  {
    "date-of-last-edit": "16.02.2025",
    "date-of-posting": "16.02.2025",
    "description": "In this description, we write what the blog post is about, like an intro, or maybe a TL;DR.",
    "post-url": "post-four",
    "preview-img-url": "/images/post_one.png",
    "tags": "#here, #we, #store, #tags",
    "title": "Post four"
  },
```
> *This is demo-data and the actual response data might vary.*

---
Endpoint: **https://alnyk.net/blog/posts/\[YOUR REQUESTED POST TITLE\]**

Results in a raw HTML response with the post itself.
It follows simple HTML markup syntax and does not utilize some form of templating.

Example response:
```HTML
<header>
  <style>
    div.title {
      background: red;
      color: var(--text);
    }
  </style>
</header>

<body>
  <h1 class="title">Post one</h1>
  <div class="date-of-posting">16.02.2025</div>
  <div class="date-of-last-edit">16.02.2025</div>
  <div class="tags">#here, #we, #store, #tags</div>
  <div class="description">
    In this description, we write what the blog post is about,
    like an intro, or maybe a TL;DR.
  </div>
  <img class="preview-img-url" src="/images/post_one.png" />
  <p>
    Here goes the main content of the post. See those classes above?
    Those are needed so that the Flask application can find them and serve
    the data inside to the front-end via JSON.
  </p>
  <p>
    Here is another paragraph, to distinguish between two paragraphs.
  </p>
</body>
```
