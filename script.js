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

document.getElementById('viewPythonCode').addEventListener('click', function() {
    // Load the Python file content dynamically
    fetch('scratchwork.py')  // Replace 'example.py' with the path to your Python file
        .then(response => response.text())
        .then(data => {
            // Display the Python code in the pre tag
            document.getElementById('pythonCodeContainer').textContent = data;
        })
        .catch(error => console.error('Error fetching Python code:', error));
});

document.getElementById('viewPythonCode').addEventListener('click', function() {
    // Load the Python file content dynamically
    fetch('scratchwork.py')  // Replace 'example.py' with the path to your Python file
        .then(response => response.text())
        .then(data => {
            // Create a data URL for the Python code
            const dataURL = 'data:text/plain;charset=utf-8,' + encodeURIComponent(data);

            // Open the Python code in a new tab
            window.open(dataURL, '_blank');
        })
        .catch(error => console.error('Error fetching Python code:', error));
});

function redirectToPage(url) {
    // Use window.location.href to redirect to the specified URL
    window.location.href = url;
}
