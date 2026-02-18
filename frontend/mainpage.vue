<template>
    <div class="mainpage">
    <navbar>
        <div class="navigationbar">
            <div class="navitem">
                <a href="/">Home</a>
            </div>
            <div class="navitem">
                <a href="/products">Products</a>
            </div>
            <div class="navitem">
                <a href="/cart">Cart</a>
            </div>
            <div class="navitem">
                <a href="/account">Account</a>
            </div>
        </div>
    </navbar>

    <herobanner>
        <div class="herobannerstyle">
            <h1>Welcome to our store!</h1>
            <p>Explore the world through our tailored loot boxes, now featuring more countries than ever!</p>
        </div>    
    </herobanner>
    </div>
</template>
<script>

</script>
<style scoped>
    .mainpage {
        display: flex;      
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    .navigationbar {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        width: 100%;
        background-color: #333;
    }

    .navitem {
        padding: 14px 20px;
        outline-color:black;
        outline-width: 2px;
        outline-style: solid;
    }

    .herobannerstyle {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 300px;
        background-color: #f2f2f2;
        text-align: center;
        color: #333;
    }
    
</style>
