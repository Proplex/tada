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

/*----------------------------------Variables----------------------------------*/
var noteZindex = 1;
var IDarray = [];
var ID = 0;
var notes;
var count  = 0;
/*----------------------------------Delete Note----------------------------------*/
function deleteNote(){
        $(this).parents('.note').remove();
        
        var deleteID = $(this).parents('.note')[0].id; // == 'noteID' + ID.toString()
        var arrayLength = IDarray.length;
        ID = arrayLength + 1;
        var index = IDarray.indexOf(deleteID);
        if (index > -1) {
            IDarray.splice(index, 1);
        }
        
        console.log($(this).parents('.note')[0].id); // print out the deleted ID                        
        console.log(IDarray);
};
/*----------------------------------Load Note----------------------------------*/
function loadNote(title, content) {
    var noteTemp =  '<div class="note" id="noteID' + ID.toString() + '">'
                        +'<a href="javascript:;" class="button remove">X</a>'
                        + 	'<div class="note_cnt" id="note_cntID' + ID.toString() + '">'
                        +		'<textarea class="title" id="note_titleID' + ID.toString() + '" placeholder="Testing title">'+title+'</textarea>'
                        + 		'<textarea class="cnt" id="note_textID' + ID.toString() + '" placeholder="Testing description">'+content+'</textarea>'
                        +	'</div> '
                        +'</div>';
    // notes.append($(noteTemp));

    // newNote.find("textarea.title").val(title);
    // newNote.find("textarea.cnt").val(content);

    $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
        function(){
            $(this).zIndex(++noteZindex);
        });
    
        $('.remove').click(deleteNote);
        $('textarea').autogrow();
                
        $('.note')
            return false; 
};
/*----------------------------------New Note----------------------------------*/
function newNote() {

    var arrayLength = IDarray.length;

    if(arrayLength < 3){
        ID = ID + 1;
                
        var noteTemp =  '<div class="note" id="noteID' + ID.toString() + '">'
                        +'<a href="javascript:;" class="button remove">X</a>'
                        + 	'<div class="note_cnt" id="note_cntID' + ID.toString() + '">'
                        +		'<textarea class="title" id="note_titleID' + ID.toString() + '" placeholder="Enter note title"></textarea>'
                        + 		'<textarea class="cnt" id="note_textID' + ID.toString() + '" placeholder="Enter note description"></textarea>'
                        +	'</div> '
                        +'</div>';

        IDarray.push('noteID'+ID.toString());
        console.log(IDarray);

        $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
            function(){
                $(this).zIndex(++noteZindex);
            });
            
            $('.remove').click(deleteNote);
            
            $('textarea').autogrow();
                
            $('.note')
                return false; 
    }
};
/*----------------------------------Save Note----------------------------------*/
function saveNote() {
        console.log('Accessing save note');
    
        var notesArray = new Array();

        // get all textarea ID for title named as note_titleID + number
        var IDtitles = $('textarea[id^="note_titleID"]').filter(
            function(){
               return this.id.match(/\d+$/);
            });

        // get all textarea ID for text named as note_textID + number
        var IDtexts = $('textarea[id^="note_textID"]').filter(
            function(){
           return this.id.match(/\d+$/);
            });
        
        for(var i = 0; i< IDtitles.length; i++){
            var tempTitle = IDtitles[i].id; // id of title of each note
            var tempText = IDtexts[i].id; // id of text of each note

            // console.log(tempTitle);
            // console.log(tempText);
            
            var eTitle = document.getElementById(tempTitle).value;
            var eText = document.getElementById(tempText).value;
                
            // console.log(eTitle);
            // console.log(eText);   

            $.ajax({
                url: '/cgi_bin/inputselector.py',
                type: "post",
                data: {"type":"note","username":"testuser","title": eTitle, "text": eText, "x": 0, "y": 0 },
                dataType: "json",
                contentType: "application/json",
                success: function() {
                  // If the JSON object was sent successfully, alert that notes are saved...
                  alert("Notes saved");      
                  console.log('Successfully saved the notes');
                }
              });

            // notesArray.push({ Index: i, Title: eTitle, Content: eText});                   
            // console.log(notesArray);
        } 
        // var arrayLength = notesArray.length;

        // for (var i = 0; i < arrayLength; i++) {
        //     var tempNote = notesArray[i];
        //     var titleofNote = tempNote.Title
        //     var contentofNote = tempNote.Content
        //     $.ajax({
        //       url: '/cgi_bin/inputselector.py',
        //       type: "post",
        //       data: {"type":"note","username":"testuser","title": titleofNote, "text": contentofNote, "x": 0, "y": 0 },
        //       dataType: "json",
        //       contentType: "application/json",
        //       success: function() {
        //         // If the JSON object was sent successfully, alert that notes are saved...
        //         alert("Notes saved");      
        //         console.log('Successfully saved the notes');
        //       }
        //     });
        // }
};

// has to populate stored data from the database
$(document).ready(function() {
    
    $("#board").height($(document).height());

    $.ajax({
        url: 'http://localhost:5000/login',
        type: "post",
        data: JSON.stringify({"username": username}),
        dataType: "json",
        contentType: "application/json",
        success: function(userData) {
          document.getElementById("navbar").style.display = "";
          document.getElementById("noteCalendarDivision").style.display = "";
          document.getElementById("startupPage").style.display = "none";
      
          for (i = 0; i < userData.notes.length; i++) {
            loadNote(userData.notes[i].title, userData.notes[i].text);
          }
        },
        error: function(response) {
          console.log(response);
        },
    });

    // notes = $("#notes"); 
    // notes = $("#board"); // get references to the 'notes' list

    $("#add_new").click(newNote);  
    
    $("#save_note").click(saveNote);

    return false;
});