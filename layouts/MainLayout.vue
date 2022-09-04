<template>
  <q-layout view="lHh Lpr lFf">
    <q-header >
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
         SANTANU
        </q-toolbar-title>

      </q-toolbar>
    </q-header>

   <q-drawer
        v-model="leftDrawerOpen"
        show-if-above
        :width="200"
        :breakpoint="600"
      >
        <q-scroll-area class="fit">
          <q-list padding class="menu-list">
            <q-item 
            to="/"
            exact
            clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="home" />
              </q-item-section>

              <q-item-section>
                Home
              </q-item-section>
            </q-item>

            <q-item
            to="/about"
            exact
             clickable v-ripple >
              <q-item-section avatar>
                <q-icon name="info" />
              </q-item-section>



              <q-item-section>
                About
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
      </q-drawer>

    <q-page-container>
      <keep-alive>
      </keep-alive>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name:'MainLayout',
  
  data() {
    return{
      leftDrawerOpen: false
    }
  }
}
</script>

