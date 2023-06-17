console.log('Main JS!');
// important links: 
// https://getbootstrap.com/docs/5.0/forms/form-control/#datalists
// https://dselect.vercel.app/
// https://github.com/devbridge/jquery-Autocomplete

const socket = io('/');

const football_players = window.football_players
console.log(football_players)
let player_ids = []
let attr = "overall_rating"

const el = document.getElementById('alt-chart');
const player_input = $("#player-search-input")
const main_form = $("#mainForm")
const selected_players = $("#selected-players")
const attr_select = $("#attr-select")

const time_server_render = (json)=>{
    render_plot(json)
    console.timeEnd("time_server_render")
}
const getThings = (arr,key)=>{
    let result=[]
    arr.forEach(element => {
        result.push(element[key])
    });
    return result
}
const render_plot=(json)=>{
    var spec = json
    var embedOpt = {
        "mode": "vega-lite",
        "actions": false // https://github.com/vega/vega-embed#options
    };
    function showError(el, error){
        el.innerHTML = ('<div class="error" style="color:red;">'
                        + '<p>JavaScript Error: ' + error.message + '</p>'
                        + "<p>This usually means there's a typo in your chart specification. "
                        + "See the javascript console for the full traceback.</p>"
                        + '</div>');
        throw error;
    }
    vegaEmbed("#alt-chart", spec, embedOpt)
        .catch(error => showError(el, error));
}
const on_change=(player_ids,attribute)=>{
    if(player_ids.length!==0){
        console.time("time_server_render")
        socket.emit("alt_chart",json=[player_ids,attribute],callback=time_server_render)
    }else{
        console.log("Couldn't update plot because there are no selected players")
    }
}
const add_player = (id,name)=>{
    console.log('User selected',name)
    player_input.val("")
    if(!player_ids.includes(id)){
        player_ids.push(id);
        let badge=$(`<span class="badge bg-primary" data-id="${id}">${name}</span>`)
        let close_button = $(`<button type="button" class="btn-close" aria-label="Close"></button>`)
        close_button.on("click",(_)=>{
            console.log(name,"was removed")
            badge.remove()
            delete_player(id,name)
        })
        badge.append(close_button)
        selected_players.append(badge)
    }
    on_change(player_ids,attr)
}
const delete_player=(id,name)=>{
    player_ids = player_ids.filter((x)=>{
        return x!==id
    })
    on_change(player_ids,attr)
}
// start-up code
$("#player-search-input").autocomplete({
    lookup:football_players,
    //lookupLimit:5,
    onSelect:(sugg)=>{
        add_player(sugg.data,sugg.value)
    },
    showNoSuggestionNotice:true,
    tabDisabled:true
})
attr_select.val(attr)
//----------------------------------------------------------------
socket.on("connect",()=>{
    console.log('Connected to server!');
    //on_change(["35724","30981","30893"],"overall_rating")
})
main_form.submit((event)=>{
    event.preventDefault();
    let player_name=player_input.val()
    let index=football_players.findIndex((x)=>{
        return x["value"].toLocaleLowerCase()===player_name
    })
    if(index>-1){
        let safe_name=football_players[index]["value"]
        let player_id=football_players[index]["data"]
        add_player(player_id, safe_name)
    }else{//player doesn't exist
        alert("Player not found") //to-do: find something better than alert
    }
    return true
})
attr_select.on("change",(event)=>{
    console.log("Atrribute changed to",event.target.value)
    attr=event.target.value
    on_change(player_ids,attr)
})
