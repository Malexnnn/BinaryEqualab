import React, { useEffect, useRef, useState } from 'react';
import { Play, Pause, RefreshCw, ZoomIn, ZoomOut, Settings2, Share2, MousePointer2, Move, LineChart, CircleDot } from 'lucide-react';
import StandardGraphing from './StandardGraphing';

type GraphMode = 'standard' | 'epicycles';
type WaveType = 'square' | 'triangle' | 'sawtooth' | 'custom';

const EpicyclesMode: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  // Animation State
  const [isPlaying, setIsPlaying] = useState(true);
  const timeRef = useRef({ t: 0 });
  const pathRef = useRef<{ x: number, y: number }[]>([]);

  // Simulation Parameters (Refs for loop performance, State for UI)
  const [numCircles, setNumCircles] = useState(5);
  const numCirclesRef = useRef(5);
  const [speed, setSpeed] = useState(1);
  const speedRef = useRef(1);
  const [waveType, setWaveType] = useState<WaveType>('square');
  const waveTypeRef = useRef<WaveType>('square');

  // Viewport State (Refs for smooth 60fps interaction)
  const zoomRef = useRef(1);
  const panRef = useRef({ x: 0, y: 0 });
  const isDraggingRef = useRef(false);
  const lastMousePosRef = useRef({ x: 0, y: 0 });

  // Helper to force re-render for UI zoom level display if needed (optional)
  const [, setTick] = useState(0);

  // Sync refs with state controls
  useEffect(() => { numCirclesRef.current = numCircles; }, [numCircles]);
  useEffect(() => { speedRef.current = speed; }, [speed]);
  useEffect(() => { waveTypeRef.current = waveType; }, [waveType]);

  // Setup Canvas & Animation
  useEffect(() => {
    const canvas = canvasRef.current;
    const container = containerRef.current;
    if (!canvas || !container) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const resize = () => {
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
      // Reset path on resize to avoid weird jumps? Or keep it? Keeping it is fine in world space.
    };
    window.addEventListener('resize', resize);
    resize();

    // pathRef.current = []; // Optional: Clear path on init

    // We'll use requestAnimationFrame instead of anime.js for the main loop to handle dynamic speed/zoom/pan better

    let animationFrameId: number;
    let lastTime = performance.now();

    const render = (now: number) => {
      if (!ctx) return;
      const dt = (now - lastTime) * speedRef.current;
      lastTime = now;

      if (isPlaying) {
        timeRef.current.t += dt * 0.001;
      }

      draw(ctx, canvas.width, canvas.height, timeRef.current.t);
      animationFrameId = requestAnimationFrame(render);
    };
    render(lastTime);

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, [isPlaying]); // Re-run if play state changes (to stop/start time integration? No, handle in loop)

  // Interactive Handlers
  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const zoomIntensity = 0.001;
    const delta = -e.deltaY * zoomIntensity;
    const newZoom = Math.min(Math.max(0.1, zoomRef.current + delta), 10);

    // Zoom towards mouse pointer
    const rect = canvasRef.current!.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    // Convert mouse to world space before zoom
    // World = (Screen - Center - Pan) / Zoom
    const cx = canvasRef.current!.width / 2;
    const cy = canvasRef.current!.height / 2;

    const worldX = (mouseX - cx - panRef.current.x) / zoomRef.current;
    const worldY = (mouseY - cy - panRef.current.y) / zoomRef.current;

    zoomRef.current = newZoom;

    // Adjust pan to keep world point under mouse
    // NewPan = Mouse - Center - World * NewZoom
    panRef.current.x = mouseX - cx - worldX * newZoom;
    panRef.current.y = mouseY - cy - worldY * newZoom;

    setTick(t => t + 1); // Trigger UI update for zoom level
  };

  const handleMouseDown = (e: React.MouseEvent) => {
    isDraggingRef.current = true;
    lastMousePosRef.current = { x: e.clientX, y: e.clientY };
    if (containerRef.current) containerRef.current.style.cursor = 'grabbing';
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDraggingRef.current) return;
    const dx = e.clientX - lastMousePosRef.current.x;
    const dy = e.clientY - lastMousePosRef.current.y;

    panRef.current.x += dx;
    panRef.current.y += dy;
    lastMousePosRef.current = { x: e.clientX, y: e.clientY };
  };

  const handleMouseUp = () => {
    isDraggingRef.current = false;
    if (containerRef.current) containerRef.current.style.cursor = 'grab';
  };

  // The Physics/Math Drawing Logic
  const draw = (ctx: CanvasRenderingContext2D, w: number, h: number, time: number) => {
    // 1. Clear Screen
    ctx.setTransform(1, 0, 0, 1, 0, 0); // Reset transform
    ctx.fillStyle = '#171513';
    ctx.fillRect(0, 0, w, h);

    // 2. Apply Camera Transform (Pan/Zoom)
    const cx = w / 2;
    const cy = h / 2;
    ctx.translate(cx + panRef.current.x, cy + panRef.current.y);
    ctx.scale(zoomRef.current, zoomRef.current);

    // 3. Draw World Grid (Infinite)
    drawGrid(ctx, w, h, zoomRef.current, panRef.current.x, panRef.current.y);

    // 4. Physics Simulation (World Space: Centered at 0,0)
    // Fourier Series: Square Wave Approximation

    // We want the wave to propagate to the right, but the circles to stay at left
    const startX = -200;
    const startY = 0;

    let x = startX;
    let y = startY;
    let prevX = startX;
    let prevY = startY;

    ctx.lineWidth = 2 / zoomRef.current; // Keep line width constant on screen or let it scale? Let's scale it slightly less
    const baseLineWidth = 1.5 / Math.sqrt(zoomRef.current);

    // Epicycles - Dynamic Fourier coefficients based on wave type
    for (let i = 0; i < numCirclesRef.current; i++) {
      let n: number;
      let radius: number;
      const baseAmplitude = 100;

      switch (waveTypeRef.current) {
        case 'square':
          // Square wave: only odd harmonics, amplitude decreases as 1/n
          n = i * 2 + 1; // 1, 3, 5, 7...
          radius = baseAmplitude * (4 / (n * Math.PI));
          break;
        case 'triangle':
          // Triangle wave: only odd harmonics, amplitude decreases as 1/n², alternating signs
          n = i * 2 + 1;
          const sign = (i % 2 === 0) ? 1 : -1;
          radius = baseAmplitude * sign * (8 / (Math.PI * Math.PI * n * n));
          break;
        case 'sawtooth':
          // Sawtooth wave: all harmonics, amplitude decreases as 1/n
          n = i + 1; // 1, 2, 3, 4...
          radius = baseAmplitude * (2 / (n * Math.PI)) * (n % 2 === 0 ? -1 : 1);
          break;
        default:
          n = i * 2 + 1;
          radius = baseAmplitude * (4 / (n * Math.PI));
      }

      const angle = n * time;
      x = prevX + radius * Math.cos(angle);
      y = prevY + radius * Math.sin(angle);

      // Circle
      ctx.beginPath();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
      ctx.lineWidth = Math.max(0.5, 1 / zoomRef.current);
      ctx.arc(prevX, prevY, Math.abs(radius), 0, Math.PI * 2);
      ctx.stroke();

      // Line
      ctx.beginPath();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.lineWidth = Math.max(0.5, 1 / zoomRef.current);
      ctx.moveTo(prevX, prevY);
      ctx.lineTo(x, y);
      ctx.stroke();

      // Dot
      ctx.fillStyle = '#fff';
      ctx.beginPath();
      ctx.arc(x, y, 2 / zoomRef.current, 0, Math.PI * 2);
      ctx.fill();

      prevX = x;
      prevY = y;
    }

    // Add point to path
    // We need to manage path length. 
    // Optimization: We only push points occasionally or prune efficiently.
    pathRef.current.push({ x, y });
    if (pathRef.current.length > 800) pathRef.current.shift();

    // Draw Path
    if (pathRef.current.length > 1) {
      ctx.beginPath();
      ctx.moveTo(pathRef.current[0].x, pathRef.current[0].y);
      for (let p of pathRef.current) {
        ctx.lineTo(p.x, p.y);
      }

      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 3 / zoomRef.current;
      ctx.strokeStyle = '#EA580C';
      ctx.stroke();

      // Glow (Expensive, maybe disable if zoom < 0.5)
      if (zoomRef.current > 0.5) {
        ctx.shadowBlur = 10;
        ctx.shadowColor = '#EA580C';
        ctx.stroke();
        ctx.shadowBlur = 0;
      }
    }

    // Connect last circle to graph
    // Let's draw the wave projection to the right
    const waveOffsetX = 100;
    // We can draw the historical 'y' values as a static wave to the right? 
    // Or just a line connecting.
    ctx.beginPath();
    ctx.setLineDash([5 / zoomRef.current, 5 / zoomRef.current]);
    ctx.strokeStyle = 'rgba(234, 88, 12, 0.3)';
    ctx.moveTo(x, y);
    ctx.lineTo(x + 200, y);
    ctx.stroke();
    ctx.setLineDash([]);
  };

  const drawGrid = (ctx: CanvasRenderingContext2D, w: number, h: number, zoom: number, panX: number, panY: number) => {
    // Calculate visible world bounds
    // Center is 0,0
    // Viewport: -w/2 to w/2
    const cx = w / 2;
    const cy = h / 2;

    const left = (-cx - panX) / zoom;
    const right = (cx - panX) / zoom;
    const top = (-cy - panY) / zoom;
    const bottom = (cy - panY) / zoom;

    // Grid spacing
    const step = 50;

    ctx.lineWidth = 1 / zoom;
    ctx.strokeStyle = '#2f2b26';

    ctx.beginPath();
    // Vertical
    const startX = Math.floor(left / step) * step;
    for (let i = startX; i < right; i += step) {
      ctx.moveTo(i, top);
      ctx.lineTo(i, bottom);
    }
    // Horizontal
    const startY = Math.floor(top / step) * step;
    for (let i = startY; i < bottom; i += step) {
      ctx.moveTo(left, i);
      ctx.lineTo(right, i);
    }
    ctx.stroke();

    // Axes
    ctx.lineWidth = 2 / zoom;
    ctx.strokeStyle = '#57534e';
    ctx.beginPath();
    ctx.moveTo(left, 0); ctx.lineTo(right, 0);
    ctx.moveTo(0, top); ctx.lineTo(0, bottom);
    ctx.stroke();
  };

  const resetView = () => {
    zoomRef.current = 1;
    panRef.current = { x: 0, y: 0 };
    setTick(t => t + 1);
  };

  return (
    <div className="flex flex-col lg:flex-row h-full bg-aurora-bg text-aurora-text overflow-hidden">

      {/* Sidebar Controls */}
      <div className="w-full lg:w-80 bg-aurora-surface/50 backdrop-blur-sm border-r border-white/5 flex flex-col z-20 shrink-0 shadow-xl">
        <div className="p-5 border-b border-white/5 flex justify-between items-center bg-aurora-panel/30">
          <h2 className="text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
            <Settings2 size={16} className="text-aurora-primary" />
            Physics Engine
          </h2>
          <span className="text-xs px-2 py-0.5 rounded bg-aurora-primary/20 text-aurora-primary border border-aurora-primary/30 font-mono animate-pulse">
            LIVE
          </span>
        </div>

        <div className="p-5 space-y-8 overflow-y-auto custom-scrollbar">
          {/* Series Control */}
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <label className="text-xs font-bold text-aurora-muted uppercase">Harmonics (N)</label>
              <span className="px-2 py-0.5 rounded-md bg-white/5 font-mono text-xs text-aurora-primary">{numCircles}</span>
            </div>
            <input
              type="range" min="1" max="100" step="1"
              value={numCircles}
              onChange={(e) => {
                setNumCircles(parseInt(e.target.value));
                pathRef.current = [];
              }}
              className="w-full h-1.5 bg-aurora-panel rounded-lg appearance-none cursor-pointer accent-aurora-primary hover:accent-aurora-primaryHover"
            />
          </div>

          {/* Speed Control */}
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <label className="text-xs font-bold text-aurora-muted uppercase">Time Dilation</label>
              <span className="px-2 py-0.5 rounded-md bg-white/5 font-mono text-xs text-aurora-primary">{speed.toFixed(1)}x</span>
            </div>
            <input
              type="range" min="0.1" max="5.0" step="0.1"
              value={speed}
              onChange={(e) => setSpeed(parseFloat(e.target.value))}
              className="w-full h-1.5 bg-aurora-panel rounded-lg appearance-none cursor-pointer accent-aurora-primary hover:accent-aurora-primaryHover"
            />
          </div>

          {/* Wave Type Selector */}
          <div className="space-y-3">
            <label className="text-xs font-bold text-aurora-muted uppercase">Wave Form</label>
            <div className="grid grid-cols-3 gap-2">
              {(['square', 'triangle', 'sawtooth'] as WaveType[]).map((type) => (
                <button
                  key={type}
                  onClick={() => { setWaveType(type); pathRef.current = []; }}
                  className={`py-2 px-3 text-xs font-bold rounded-lg transition-all border ${waveType === type
                    ? 'bg-aurora-primary text-white border-aurora-primary shadow-lg'
                    : 'bg-white/5 text-aurora-muted border-white/10 hover:bg-white/10 hover:text-white'
                    }`}
                >
                  {type === 'square' && '▭'}
                  {type === 'triangle' && '△'}
                  {type === 'sawtooth' && '⋸'}
                  <span className="ml-1 capitalize">{type}</span>
                </button>
              ))}
            </div>
          </div>

          {/* View Info */}
          <div className="space-y-2 pt-4 border-t border-white/5">
            <div className="flex justify-between text-xs font-mono text-aurora-muted">
              <span>ZOOM</span>
              <span>{Math.round(zoomRef.current * 100)}%</span>
            </div>
            <div className="flex justify-between text-xs font-mono text-aurora-muted">
              <span>PAN X</span>
              <span>{Math.round(panRef.current.x)}</span>
            </div>
            <div className="flex justify-between text-xs font-mono text-aurora-muted">
              <span>PAN Y</span>
              <span>{Math.round(panRef.current.y)}</span>
            </div>
            <button onClick={resetView} className="w-full mt-2 py-1.5 text-xs border border-white/10 rounded hover:bg-white/5 transition-colors">
              Reset Camera
            </button>
          </div>

          {/* Expression Info */}
          <div className="p-4 rounded-xl bg-aurora-panel border border-white/5 shadow-inner">
            <div className="flex items-center gap-2 mb-2">
              <div className="size-2 rounded-full bg-aurora-primary"></div>
              <span className="text-xs font-bold text-white capitalize">{waveType} Wave Series</span>
            </div>
            <div className="font-mono text-xs text-aurora-muted break-all">
              {waveType === 'square' && 'f(t) = 4/π ∑ (sin(nt)/n), n=1,3,5...'}
              {waveType === 'triangle' && 'f(t) = 8/π² ∑ ((-1)^k sin(nt)/n²), n=1,3,5...'}
              {waveType === 'sawtooth' && 'f(t) = 2/π ∑ ((-1)^n sin(nt)/n), n=1,2,3...'}
            </div>
            <div className="mt-2 text-[10px] text-emerald-500 flex items-center gap-1">
              <RefreshCw size={10} className="animate-spin" /> Rendering at 60 FPS
            </div>
          </div>
        </div>
      </div>

      {/* Canvas Area */}
      <div
        className="flex-1 relative h-full bg-[#111] overflow-hidden select-none"
        ref={containerRef}
        style={{ cursor: 'grab' }}
      >
        <canvas
          ref={canvasRef}
          className="block w-full h-full"
          onWheel={handleWheel}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseUp}
        />

        {/* Floating Controls */}
        <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-2 p-2 rounded-2xl bg-aurora-panel/90 backdrop-blur-md border border-white/10 shadow-2xl z-30">
          <button
            onClick={() => { zoomRef.current = Math.max(0.1, zoomRef.current - 0.2); setTick(t => t + 1); }}
            className="p-3 rounded-xl hover:bg-white/10 text-white transition-colors"
            title="Zoom Out"
          >
            <ZoomOut size={20} />
          </button>
          <div className="w-px h-6 bg-white/10"></div>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="size-12 rounded-xl bg-aurora-primary text-white flex items-center justify-center hover:bg-aurora-primaryHover shadow-[0_0_15px_rgba(234,88,12,0.4)] transition-all active:scale-95"
          >
            {isPlaying ? <Pause size={24} fill="currentColor" /> : <Play size={24} fill="currentColor" className="ml-1" />}
          </button>
          <div className="w-px h-6 bg-white/10"></div>
          <button
            onClick={() => { zoomRef.current = Math.min(10, zoomRef.current + 0.2); setTick(t => t + 1); }}
            className="p-3 rounded-xl hover:bg-white/10 text-white transition-colors"
            title="Zoom In"
          >
            <ZoomIn size={20} />
          </button>
        </div>

        {/* Overlay Info */}
        <div className="absolute top-6 right-6 flex flex-col items-end pointer-events-none opacity-50 hover:opacity-100 transition-opacity">
          <h1 className="text-2xl font-bold text-white/20 select-none">CANVAS RENDERER</h1>
          <div className="flex items-center gap-4 text-white/30 font-mono text-xs mt-1">
            <span className="flex items-center gap-1"><MousePointer2 size={12} /> Pan</span>
            <span className="flex items-center gap-1"><Move size={12} /> Zoom</span>
          </div>
        </div>
      </div>
    </div>
  );
};

// Wrapper component with mode toggle
const GraphingMode: React.FC = () => {
  const [mode, setMode] = useState<GraphMode>('standard');

  return (
    <div className="h-full flex flex-col">
      {/* Mode Toggle */}
      <div className="flex items-center gap-2 p-3 bg-background-light border-b border-aurora-border shrink-0">
        <span className="text-xs text-aurora-muted uppercase tracking-wider mr-2">Mode:</span>
        <button
          onClick={() => setMode('standard')}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${mode === 'standard'
            ? 'bg-primary text-white shadow-lg'
            : 'bg-background hover:bg-background-light text-aurora-text border border-aurora-border'
            }`}
        >
          <LineChart size={16} />
          Standard
        </button>
        <button
          onClick={() => setMode('epicycles')}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${mode === 'epicycles'
            ? 'bg-primary text-white shadow-lg'
            : 'bg-background hover:bg-background-light text-aurora-text border border-aurora-border'
            }`}
        >
          <CircleDot size={16} />
          Epicycles
        </button>
      </div>

      {/* Content */}
      <div className="flex-1 overflow-hidden">
        {mode === 'standard' ? <StandardGraphing /> : <EpicyclesMode />}
      </div>
    </div>
  );
};

export default GraphingMode;