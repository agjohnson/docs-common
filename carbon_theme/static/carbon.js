
function getQueryStringParams (sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&');

    for (var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
}


$(document).ready(function () {
    // Highlight page in top nav
    var highlightLink;
    $(".js-header-link").each(function (i, node) {
        var lastURISegment  = window.location.href.substr(window.location.href.lastIndexOf('/') + 1).split("?")[0],
            href            = $(node).attr("href"),
            lastHrefSegment = href.substr(href.lastIndexOf('/') + 1);
        
        if (lastURISegment === lastHrefSegment) {
            highlightLink = $(node);

        } else if (!highlightLink) {
            highlightLink = $(".js-header-link.m-docs");
        }
    });

    highlightLink.addClass("s-active");

    // Scroll sidebar to location in URL query string
    if (getQueryStringParams("navScrollTop")) {
        $(".wy-nav-side").scrollTop(getQueryStringParams("navScrollTop"));
    }

    var header_height = $('header#mlab-header').height();

    function scroll_to_id(id) {
        var elem = $(id);
        if (elem) {
            $('html, body').animate({
                scrollTop: elem.offset().top - header_height - 20
            }, 350);
        }
    }

    $(".wy-nav-side a").click(function (event, node) {
        event.preventDefault();

        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);
                scroll_to_id(this.hash);
            }

            else {
                location.hash = this.hash;
            }
        
        } else {
           var scrollTop = $(".wy-nav-side").scrollTop(),
               href      = $(event.target).attr("href") + "?navScrollTop=" + scrollTop;

           window.location.href = href;
        }
    });

    // Override default action on link elements when the href is an anchor.
    // Avoid the hashchange event altogether, as it will flicker -- scroll to
    // where the browser thinks we should be first, then our real position via
    // the call to scroll_to_id
    $('.wy-nav-content a').on('click', function (event) {
        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);
                scroll_to_id(this.hash);
            }
            else {
                location.hash = this.hash;
            }
            event.preventDefault();
        }
    });

    // Triger after timeout because we can't prevent the default action of a
    // hashchange on page load
    $(window).on('hashchange', function () {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    });

    // Initial trigger, if there is a hash in the URL
    if (window.location.hash) {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    }

    // Mobile menu
    $('header#mlab-header div.mobile-menu a').on('click', function(event) {
        $('header#mlab-header').toggleClass('shift');
        event.preventDefault();
    })

    // Override scrolling from theme
    SphinxRtdTheme.StickyNav.onScroll = function () {};

    // Syntax highlighting for '$' or '%' in shell code blocks.
    $(".highlight-sh pre").each(function (i, el) {
        $(el).html(function (i, html) {
            return html.replace(/(\$ |\% )/g, '<span class="sh-first-char">$1</span>');
        });
    });
});
