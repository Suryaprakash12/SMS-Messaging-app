/** 
console.log('hii')
const Message=document.getElementById('message');
console.log(Message)

const idbody=document.getElementById('id_body');
const csrf=document.getElementsByName('csrfmiddlewaretoken')
console.log(idbody);
console.log(csrfmiddlewaretoken)

Message.addEventListener('submit',e=>
{
    e.preventDefault()
    $.ajax
    {
        type:'POST',
        url: Message.action,
        data:
        {
            'csrfmiddlewaretoken':csrf[0].value,
            'body':body.value,
        },
        success:function(response)
        {
            console.log(response);
        },
        error:function(error)
        {
            console.log(error);
        }


    }
}
)
**/