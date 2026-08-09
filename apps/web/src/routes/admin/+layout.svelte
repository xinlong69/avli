<script lang="ts">
  import { resolve } from '$app/paths';

  /** * Svelte 5 "Runes" Syntax:
   * $props() is how we receive data passed to this component.
   * 'children' is a special snippet that represents the page content 
   * (e.g., whatever is in your +page.svelte).
   */
  let { children } = $props();
  let isCollapsed = $state(false);

  function toggleSidebar() {
    isCollapsed = !isCollapsed;
  }
</script>

<div class="flex min-h-screen bg-base-200">
  <aside 
    class="bg-base-100 border-r border-base-200 transition-[width] duration-300 flex flex-col z-20
    {isCollapsed ? 'w-20' : 'w-64'}"
  >
    <div class="p-4 flex items-center {isCollapsed ? 'justify-center' : 'justify-between'} min-h-[64px]">
      {#if !isCollapsed}
        <span class="font-bold text-xl px-2 transition-opacity">Admin Panel</span>
      {/if}
      <button 
        class="btn btn-ghost btn-square btn-sm" 
        onclick={toggleSidebar}
        aria-label={isCollapsed ? "Expand sidebar" : "Collapse sidebar"}
      >
        <span class="icon-[heroicons-outline--bars-3-bottom-left] w-6 h-6"></span>
      </button>
    </div>

    <ul class="menu px-2 space-y-2 w-full">
      <li class="flex items-center {isCollapsed ? 'justify-center' : ''}">
        <span 
          class="menu-title opacity-50 text-xs uppercase tracking-widest px-4 w-full min-h-[1.25rem] flex items-center"
        >
          {#if !isCollapsed}
            Admin
          {/if}
        </span>
      </li>
      <li>
        <a 
          href={resolve("/admin")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Admin">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--chart-bar] w-6 h-6"></span>
          </div>
          {#if !isCollapsed} 
            <span class="whitespace-nowrap font-medium">Admin</span> 
          {/if}
        </a>
      </li>
      <li>
        <a 
          href={resolve("/admin/users")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Users">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--cog-6-tooth] w-6 h-6"></span>
          </div>
          {#if !isCollapsed} 
            <span class="whitespace-nowrap font-medium">Users</span> 
          {/if}
        </a>
      </li>
      <li>
        <a 
          href={resolve("/")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Back to Site">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--user] w-6 h-6"></span>
          </div>
          {#if !isCollapsed}
            <span class="whitespace-nowrap font-medium">Back to Site</span> 
          {/if}
        </a>
      </li>
    </ul>
	</aside>

  <div class="flex-1 flex flex-col min-w-0">
    <header class="navbar bg-base-100 border-b border-base-200 px-4">
      <div class="flex-1">
        {#if isCollapsed}
          <span class="font-bold text-xl tracking-tight mr-2 transition-opacity hidden md:block">Admin Panel</span>
        {/if}
      </div>
      <div class="flex-1"></div>
    </header>
    <main class="p-6 overflow-auto">
      {@render children()}
    </main>
  </div>
</div>