# NOTES

Current ideas for implementing a back-end for the blog-page.

## FOR THE FRONT BLOG-PAGE (WHERE ALL THE BLOGS ARE ORGANIZED)

Use Flask to serve JSON with:
  1. All API endpoints for posts
  2. Title / header
  3. Thumbnail / preview (as src links to the backend)
  4. Tags
  5. Introduction / TL;DR

## HOW TO GO ABOUT GETTING JSON DATA FROM THE MARKDOWN FILES THEMSELVES,
*TO AVOID HAVING TO MANUALLY WRITE THE JSON FILES TO BE SERVED MANUALLY?*

Write some code to fetch the following contents from the MD files.
  CON:
    - I would have to use some static MD template to make the MD file predictable for the program.
  PRO:
    - I can dynamically edit the files and the update on the client-side would be immediate.

## STUFF TO KEEP IN MIND WHEN WRITING THIS:
  1. Some system to keep up with tags on posts.
  2. Write own markdown, or specify my own style in "marko"?
  3. How to go about if I want some cool feature on the site, like a scrollable image-album for the keyboard-post?

## PER BLOG POST (THE POSTS THEMSELVES):
  - Use Flask to serve static HTML, already prepared the styling on the client-side with Vue.
