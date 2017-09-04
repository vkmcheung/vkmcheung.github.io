---
layout: default
---

## Personal

---

This page contains some more about me besides work.

I envision this page to be more like a blog, with dated postings and possibly hash tags for different topics. Things will start appearing once I get my head around how to set this up.

_Note: The lack of information in this page does not reflect the reality of my work-life balance!_




<div class="posts">
  {% for post in site.posts %}
    <article class="post">

      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

      <div class="entry">
        {{ post.excerpt }}
      </div>

      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
    </article>
  {% endfor %}
</div>




<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

For now, you might be interested in this:

### Why I don't call myself a PhD student
Short answer: Because I'm studying for a [Dr. rer. nat (_Doctor rerum naturalium_)](https://en.wikipedia.org/wiki/Dr._rer._nat.) and not a PhD.

Long answer: There was a time when the natural sciences (along with the arts and humanities) were considered to be a part of philosophy, and people who did research, wrote, and successfully defended a thesis on their work were conferred with the title of _Doctor of Philosophy_. But from 1863 with the University of Tübingen, people doing natural sciences broke away from the faculty of philosophy in German universities and started their own faculty. This was soon followed by other disciplines such as engineering and economics. The end result was that those who pursued a doctorate received the academic title based on their field of research. Those working in the natural sciences would earn a [Dr. rer. nat (_Doctor rerum naturalium_)](https://en.wikipedia.org/wiki/Dr._rer._nat.), or doctor of natural sciences; Similarly, those in economics would get a _Dr. oec._ (_oeconomiae_ being _economics_ in Latin), and engineering _Dr.-Ing_ (_-Ing_ standing for _Ingenieur_ or _engineer_ in German). You can read more about this [here](http://www.biospektrum.de/blatt/d_bs_pdf&_id=1008689) (only in German). Although most graduate students in German universities nowadays have the option of graduating with a PhD, I thought it would be a nice way to reflect my graduate research training in Germany by having it in my (eventual) academic title. That's why I opted for a _Dr. rer. nat._ and not a _PhD_.

But for matters of convenience, I still often call myself a PhD student!

<br><br>[Back to [home](index.md)]
