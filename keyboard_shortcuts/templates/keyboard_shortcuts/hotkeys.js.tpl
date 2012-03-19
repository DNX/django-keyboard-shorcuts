<script type="text/javascript">
    var hotkeys = {{ hotkeys|safe }};
    var special_disabled = {{ special_disabled|lower }};
    var pressed_keys = new Array()
    var func = function(event) {
        var target;
        event = event || window.event;
        code = event.keyCode || event.which;
        // check if we are in input
        if (event.target) target = event.target;
        else if (event.srcElement) target = event.srcElement;
        if (target.nodeType == 3) // defeat Safari bug
                target = target.parentNode;
        if (special_disabled && (target.type === "text" || target.nodeName === "SELECT" || target.nodeName === "TEXTAREA")) {
            pressed_keys = [] // we reset pressed keys
            return
        }
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