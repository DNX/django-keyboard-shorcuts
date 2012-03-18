<script type="text/javascript">
    var hotkeys = {{ hotkeys|safe }};
    var pressed_keys = new Array()
    var func = function(event) {
        event = event || window.event;
        code = event.keyCode || event.which;
        combinations = hotkeys
        if (pressed_keys.length) { // we have some pressed keys
            for (array_key in pressed_keys) {
                combinations = combinations[pressed_keys[array_key]]
            }
        }
        if (code in combinations) {
            if (combinations[code]['link']) {
                window.location.href = combinations[code]['link'];
                pressed_keys = [] // we reset pressed keys
            }
            else {
                pressed_keys.push(code)
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