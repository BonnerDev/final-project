function bartest(){
    d3.json("/data").then((test) => {
        console.log(test)
    });
};
