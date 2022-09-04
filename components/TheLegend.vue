<template>
  <div class="legend dbz noselect">
    <span>dBz</span>
    <span>5</span>
    <span>10</span>
    <span>15</span>
    <span>20</span>
    <span>25</span>
    <span>30</span>
    <span>35</span>
    <span>40</span>
    <span>45</span>
    <span>50</span>
    <span>55</span>
    <span>60</span>
    <span>65</span>
    <span>70</span>
    <span>&nbsp;</span>
  </div>
 
</template>

<script>

</script>

<style>
.legend {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: aquamarine;
  position: absolute;
  bottom:25rem;
  right: 1rem;
  border-radius: 10rem;
  box-shadow: 0 0 0.3rem #333;
  z-index: 1000;
  cursor: default;
}

.dbz {
  background: linear-gradient(
    to bottom,
    #04fdff,
    #04fdff,
    #04fdff,
    #0097fe,
    #0100fe,
    #00ff03,
    #02c803,
    #029401,
    #fffd00,
    #ffc603,
    #fd7801,
    #ff0101,
    #c80000,
    #970102,
    #ff02ff,
    #9300fc,
    #9300fc
  );
}



.legend span {
  flex: 1 1 auto;
  padding: 0.09rem;
  font-size: 0.8rem;
  font-weight: 500;
  transform: translate(0, 50%);
  /* text-shadow: 0 0 1px #fff, 0 0 1px #fff, 0 0 1px #fff, 0 0 1px #fff; */
  text-shadow: -0.075rem -0.075rem 0 #fff, 0.075rem -0.075rem 0 #fff,
    -0.075rem 0.075rem 0 #fff, 0.075rem 0.075rem 0 #fff;
}


@media (min-width: 650px) {
  .legend {
    top: 7rem;
    bottom: initial;
  }
}
</style>
