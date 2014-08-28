window.onload = function() {
    var themes_list = document.getElementById("themes_list");
    var lang_list = document.getElementById("lang_list");
    var zoomInBut = document.getElementById("zoomInBut"),
        zoomOutBut = document.getElementById("zoomOutBut");

    var default_font_size = 14,
        font_size = default_font_size,
        font_size_delta = 2,
        MIN_FONT_SIZE = 8,
        MAX_FONT_SIZE = 40;

    var editor = ace.edit("editor");
    editor.setFontSize(default_font_size);

    setSelectedTheme();
    setSelectedLang();

    zoomInBut.onclick = function() {
        if(font_size < MAX_FONT_SIZE)
            editor.setFontSize(font_size += font_size_delta)
        console.log(font_size)
    }

    zoomOutBut.onclick = function() {
        if(font_size > MIN_FONT_SIZE)
            editor.setFontSize(font_size -= font_size_delta)
        console.log(font_size)
    }

    themes_list.onchange = function() {
        setSelectedTheme();
    };

    lang_list.onchange = function() {
        setSelectedLang();
    };

    function setSelectedTheme() {
        var changedTheme = themes_list.options[themes_list.selectedIndex].value;
        editor.setTheme("ace/theme/" + changedTheme);
    }

    function setSelectedLang() {
        var changedLang = lang_list.options[lang_list.selectedIndex].value;
        editor.getSession().setMode("ace/mode/javascript" + changedLang);
    }
};