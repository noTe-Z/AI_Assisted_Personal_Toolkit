javascript:(function() {
    var searchQuery = encodeURIComponent(document.getElementsByName('q')[0].value);
    var bingSearchUrl = 'https://www.bing.com/search?q=' + searchQuery;
    window.location.href = bingSearchUrl;
})();