window.onload = function() {
    var themes_list = document.getElementById("themes_list");
    var lang_list = document.getElementById("lang_list");
    var zoomInBut = document.getElementById("zoomInBut"),
        zoomOutBut = document.getElementById("zoomOutBut");
    var saveBut = document.getElementById("saveBut");

    var default_font_size = 14,
        font_size = default_font_size,
        font_size_delta = 2,
        MIN_FONT_SIZE = 8,
        MAX_FONT_SIZE = 40;

    var editor_div = document.getElementById("editor");
    var editor = ace.edit("editor");



    setSelectedTheme();
    setSelectedLang();

    saveBut.onclick = function() {
        var lang_name = lang_list.options[lang_list.selectedIndex].text;
        var lang_ext = lang_list.options[lang_list.selectedIndex].value;
        var text = editor.getSession().getValue();
        var blob = new Blob([text], {type: "text/" +
            lang_name + "; charset=utf-8"});
        saveAs(blob, "exported_file." + lang_ext);
    }

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