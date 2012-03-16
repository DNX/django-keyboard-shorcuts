<script type="text/javascript">
    var hotkeys = {{ hotkeys|safe }};
    var func = function(event) {
        event = event || window.event;
        code = event.keyCode || event.which;
        if (code in hotkeys) {
            if (hotkeys[code]['link']) {
                window.location.href = hotkeys[code]['link'];
            }
        }
        return false;
    }
    if (document.addEventListener) {
        document.addEventListener('keydown', func, false);
    } else if (document.attachEvent)  {
        document.attachEvent('keydown', func, false);
    }
</script>