<script lang="ts">
  /** * This is the LAYOUT. 
   * It stays the same when you switch between Login and Register.
   */
  let { children } = $props();
</script>

<div class="min-h-screen w-full flex items-center justify-center p-4 relative overflow-hidden bg-[#0e3a5d]">
  
  <div class="absolute inset-0 z-0">
    <div class="absolute top-[10%] left-[-10%] w-[80%] h-[80%] rounded-full bg-cyan-400/30 blur-[120px]"></div>
    
    <div class="absolute top-[-20%] right-[10%] w-[60%] h-[60%] rounded-full bg-orange-400/20 blur-[100px]"></div>
    
    <div class="absolute bottom-[-10%] left-[20%] w-[50%] h-[50%] rounded-full bg-peach-200/10 blur-[110px] bg-orange-200/20"></div>

    <div class="absolute bottom-[0%] right-[-10%] w-[70%] h-[70%] rounded-full bg-indigo-600/30 blur-[130px]"></div>
  </div>

  <div class="card w-full h-full max-w-[480px] bg-white/20 backdrop-blur-sm border border-white/30 rounded-xl shadow-2xl">
    <div class="card-body p-8 md:p-12">
      {@render children()}
    </div>
  </div>
</div>