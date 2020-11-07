console.log("hello")

var data;

d3.json("/data",(test)=>{
    console.log(test)
    Object.values(test).forEach
    ((element) => {
        console.log(element.placement_type)
    });
});
