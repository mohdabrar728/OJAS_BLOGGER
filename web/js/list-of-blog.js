async function run() {
    let n = await eel.listblog()();
    console.log(n);
    addcall(n);
}
run();


