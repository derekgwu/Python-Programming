document.addEventListener('DOMContentLoaded', function () {
    var burgerBtn = document.getElementById('burger-btn');
    var navList = document.querySelector('nav ul');
    var chapterContent = document.getElementById('chapter-content');

    burgerBtn.addEventListener('click', function () {
        navList.style.display = (navList.style.display === 'none' || navList.style.display === '') ? 'block' : 'none';
    });

    // Handle table of contents item clicks
    var tocItems = document.querySelectorAll('nav ul li a');
    tocItems.forEach(function (item) {
        item.addEventListener('click', function (event) {
            event.preventDefault();
            var chapterId = event.target.getAttribute('href').substring(1); // Extract chapter ID from href
            displayChapterContent(chapterId);
        });
    });

    var markdownContent = document.getElementById('markdown-content').innerHTML;
    var htmlContent = marked(markdownContent);
    document.getElementById('markdown-content').innerHTML = htmlContent;

    // Function to display chapter content
    function displayChapterContent(chapterId) {
        var selectedChapter = document.getElementById(chapterId);
        if (selectedChapter) {
            // Clear existing content
            chapterContent.innerHTML = '';

            // Clone and append the selected chapter's content
            var clonedContent = selectedChapter.cloneNode(true);
            chapterContent.appendChild(clonedContent);

            // Scroll to the displayed chapter content
            chapterContent.scrollIntoView({ behavior: 'smooth' });

            // Hide the table of contents
            navList.style.display = 'none';
        }
    }
});
document.addEventListener('DOMContentLoaded', function () {
    // Convert Markdown content to HTML using Marked.js
    var markdownSections = document.querySelectorAll('.markdown-content');
    
    markdownSections.forEach(function (section) {
        var markdownContent = section.innerHTML;
        section.innerHTML = marked(markdownContent);
    });
});

document.querySelectorAll('.flip-card').forEach(function(card) {
    card.addEventListener('click', function() {
      this.classList.toggle('flipped');
    });
  });

 // Add click event listeners to toggle visibility of sub-tocs
 document.addEventListener("DOMContentLoaded", function () {
    const chapters = document.querySelectorAll('.toc > li');

    chapters.forEach(chapter => {
        chapter.addEventListener('click', function () {
            const subToc = this.querySelector('.sub-toc');
            if (subToc) {
                subToc.style.display = subToc.style.display === 'none' ? 'block' : 'none';
            }
        });
    });
});
