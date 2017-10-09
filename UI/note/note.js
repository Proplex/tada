(function($)
{
    
    $.fn.autogrow = function(options)
    {
        return this.filter('textarea').each(function()
        {
            var self         = this;
            var $self        = $(self);
            var minHeight    = $self.height();
            var noFlickerPad = $self.hasClass('autogrow-short') ? 0 : parseInt($self.css('lineHeight')) || 0;

            var shadow = $('<div></div>').css({
                position:    'absolute',
                top:         -10000,
                left:        -10000,
                width:       $self.width(),
                fontSize:    $self.css('fontSize'),
                fontFamily:  $self.css('fontFamily'),
                fontWeight:  $self.css('fontWeight'),
                lineHeight:  $self.css('lineHeight'),
                resize:      'none',
                'word-wrap': 'break-word'
            }).appendTo(document.body);

            var update = function(event)
            {
                var times = function(string, number)
                {
                    for (var i=0, r=''; i<number; i++) r += string;
                    return r;
                };

                var val = self.value.replace(/</g, '&lt;')
                                    .replace(/>/g, '&gt;')
                                    .replace(/&/g, '&amp;')
                                    .replace(/\n$/, '<br/>&nbsp;')
                                    .replace(/\n/g, '<br/>')
                                    .replace(/ {2,}/g, function(space){ return times('&nbsp;', space.length - 1) + ' ' });

                // Did enter get pressed?  Resize in this keydown event so that the flicker doesn't occur.
                if (event && event.data && event.data.event === 'keydown' && event.keyCode === 13) {
                    val += '<br />';
                }

                shadow.css('width', $self.width());
                shadow.html(val + (noFlickerPad === 0 ? '...' : '')); // Append '...' to resize pre-emptively.
                $self.height(Math.max(shadow.height() + noFlickerPad, minHeight));
            }

            $self.change(update).keyup(update).keydown({event:'keydown'},update);
            $(window).resize(update);

            update();
        });
    };
})(jQuery);


var noteZindex = 1;
function deleteNote(){
        $(this).parent('.note').hide("puff",{ percent: 133}, 250);
};

function loadNote(title, content) {
    var noteTemp =  '<div class="note">'
                        +'<a href="javascript:;" class="button remove">X</a>'
                        + 	'<div class="note_cnt">'
                        +		'<textarea class="title" placeholder="Testing Title"></textarea>'
                        + 		'<textarea class="cnt" placeholder="Testing Content"></textarea>'
                        +	'</div> '
                        +'</div>';
    // notes.append($(noteTemp));

    newNote.find("textarea.title").val(title);
    newNote.find("textarea.cnt").val(content);

    $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
        function(){
            $(this).zIndex(++noteZindex);
        });
    
        $('.remove').click(deleteNote);
        $('textarea').autogrow();
                
        $('.note')
            return false; 
};

function newNote() {
    var noteTemp =  '<div class="note">'
                    +'<a href="javascript:;" class="button remove">X</a>'
                    + 	'<div class="note_cnt">'
                    +		'<textarea class="title" placeholder="Enter note title"></textarea>'
                    + 		'<textarea class="cnt" placeholder="Enter note description"></textarea>'
                    +	'</div> '
                    +'</div>';

    $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
        function(){
            $(this).zIndex(++noteZindex);
        });

        $('.remove').click(deleteNote);
        $('textarea').autogrow();
            
        $('.note')
            return false; 
};

function saveNote() {
        var notesArray = new Array();
        // for each of the notes add a bespoke note object to the array
        notes.find("li > div").each(function (i, e) {
            // save the class attribute of the div, as well as the text for the title and content text areas
            // var colourClass = $(e).attr("class");
            var title = $(e).find("textarea.title") 
            var content = $(e).find("textarea.cnt");
     
            console.log(title);
            console.log(content);
            console.log('testing');
            
            notesArray.push({ Index: i, Title: title.val(), Content: content.val()});
        });
     
        // json encode it
        var jsonStr = JSON.stringify(notesArray);
     
        // and save the json string into local storage
        localStorage.setItem("notes", jsonStr);
     
        // info the user it's done
        alert("Notes saved");
};


var notes;
var count  = 0;
// has to populate stored data from the database
$(document).ready(function() {
    
    $("#board").height($(document).height());
//     Comment out when it's pefectly working    
//     notes = $("#notes"); 
//     // notes = $("#board"); // get references to the 'notes' list
 
//     // load notes from local storage if one's available
//     var storedNotes = localStorage.getItem("notes");
//     if (storedNotes) {
//     // passes the stored json back into an array of note objects
//         var notesArray = JSON.parse(storedNotes);
//         count = notesArray.length;
 
//         for (var i = 0; i < count; i++) {
//             var storedNote = notesArray[i];
//             loadNote(storedNote.Title, storedNote.Content);
//         }
// }

    $("#add_new").click(newNote);  
    
    $("#save_note").click(saveNote);

    return false;
});


    // alert("Top: " + getOffset(note1).left + " Left: " + getOffset(note1).right);
    // getOffset(newNote).left;
    // getOffset(newNote).right;
    
// $("button").click(function(){
//     var x = $("p").position();
//     alert("Top: " + x.top + " Left: " + x.left);
// });

