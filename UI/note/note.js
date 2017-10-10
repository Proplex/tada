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
var IDarray = []; // keep track of which note is present and which is deleted
var checkID = []; 
/*----------------------------------Delete Note----------------------------------*/
function deleteNote(){
    $(this).parents('.note').remove(); // remove the note on click of corresponding x button
        
    var deleteID = $(this).parents('.note')[0].id; // == get 'noteID' + ID.toString() of deleted note
    var index = IDarray.indexOf(deleteID); // get index of deleted note's ID
    if (index > -1) {
        IDarray.splice(index, 1); // remove the deleted note's ID from the ID array
    }
        
    console.log('Deleted ID: ' + $(this).parents('.note')[0].id); // print out the deleted ID                        
    console.log('ID array: ' + IDarray); // print out current ID array
};
/*----------------------------------Load Note----------------------------------*/
function loadNote(title, content, ID) {
    ID = parseInt(ID); // convert ID from string to int
    var noteTemp =  '<div class="note" id="noteID' + ID.toString() + '">'
                        +'<a href="javascript:;" class="button remove">X</a>'
                        + 	'<div class="note_cnt" id="note_cntID' + ID.toString() + '">'
                        +		'<textarea class="title" id="titleID' + ID.toString() + '" placeholder="Testing title">'+title+'</textarea>'
                        + 		'<textarea class="cnt" id="textID' + ID.toString() + '" placeholder="Testing description">'+content+'</textarea>'
                        +	'</div> '
                        +'</div>';

    IDarray.push('noteID' + ID.toString()); // push the added note's ID into the ID array
    console.log('ID array: ' + IDarray); // print out current ID array
    checkID.push(ID.toString());

    $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
        function(){
            $(this).zIndex(++noteZindex);
        }); // show the loaded note to the UI
    
    $('.remove').click(deleteNote); // onclick of delete button, trigger the deleteNote function
    $('textarea').autogrow(); // text area grows automatically       
    $('.note')
    return false; 
};
/*----------------------------------New Note----------------------------------*/
function newNote() {

    var arrayLength = IDarray.length;

    if(arrayLength < 3){

        var ID = Math.floor((Math.random() * 1000) + 1); // random number between 1 and 1000
        
        var noteTemp =  '<div class="note" id="noteID' + ID.toString() + '">'
                        +'<a href="javascript:;" class="button remove">X</a>'
                        + 	'<div class="note_cnt" id="note_cntID' + ID.toString() + '">'
                        +		'<textarea class="title" id="titleID' + ID.toString() + '" placeholder="Enter note title"></textarea>'
                        + 		'<textarea class="cnt" id="textID' + ID.toString() + '" placeholder="Enter note description"></textarea>'
                        +	'</div> '
                        +'</div>';

        IDarray.push('noteID' + ID.toString()); // push the added note's ID into the ID array
        console.log('ID array: ' + IDarray); // print out current ID array
                        
        $(noteTemp).hide().appendTo("#board").show("fade", 300).draggable().on('dragstart',
            function(){
                $(this).zIndex(++noteZindex);
            }); // show the new note to the UI
            
        $('.remove').click(deleteNote); // onclick of delete button, trigger the deleteNote function
        $('textarea').autogrow(); // text area grows automatically              
        $('.note')
        return false; 
    }
};
/*----------------------------------Save Note----------------------------------*/
function saveNote() {
    console.log('Saving notes...');

    // get all textarea ID for title named as titleID + number
    var IDtitles = $('textarea[id^="titleID"]').filter(
        function(){
            return this.id.match(/\d+$/);
        });

    // get all textarea ID for text named as textID + number
    var IDtexts = $('textarea[id^="textID"]').filter(
        function(){
           return this.id.match(/\d+$/);
        });
        
    for(var i = 0; i< IDtitles.length; i++){
        var checksum = 0;

        var tempTitle = IDtitles[i].id; // id of title of each note
        var tempText = IDtexts[i].id; // id of text of each note

        // console.log('Saved titleID: ' + tempTitle); 
        // console.log('Saved textID: ' + tempText);
            
        var eTitle = document.getElementById(tempTitle).value; // get the value inside of the textarea.title of each note
        var eText = document.getElementById(tempText).value; // get the value inside of the textarea.text of each note
        var eID = tempTitle.replace('titleID',''); // extract only the ID string from the string of titleID (for loadNote)
                
        console.log('Saved ID: ' + eID);           
        console.log('Saved title: ' + eTitle);
        console.log('Saved text: ' + eText);

        
        for(var j = 0; j < checkID.length; j++){
            if(checkID[j] == eID){
                checksum = 1; // don't send the data to dabase since it already exists
            }
        }

        if(checksum == 0){
            var toSend = {"type":"note","username":username,"title": eTitle, "text": eText, "x": 0, "y": 0, "noteID": eID}
            
            $.ajax({
                url: 'http://localhost:5000/add',
                type: "post",
                data: JSON.stringify(toSend),
                dataType: "json",
                contentType: "application/json",
                success: function() {
                // If the JSON object was sent successfully, alert that notes are saved...
                console.log('Successfully saved the notes');
                }   
            });
        }
    } 
};
