import React, { useState } from 'react';
import { User, Settings, Bell, Search, LogIn, LogOut } from 'lucide-react';
import { useCalculator, AngleMode } from '../CalculatorContext';
import { useAuth } from '../contexts/AuthContext';
import AuthModal from './AuthModal';

const TopBar: React.FC = () => {
   const { angleMode, setAngleMode } = useCalculator();
   const { user, loading, signOut } = useAuth();
   const [showAuthModal, setShowAuthModal] = useState(false);
   const modes: AngleMode[] = ['DEG', 'RAD', 'GRAD'];

   return (
      <>
         <header className="h-16 bg-background/80 backdrop-blur-md border-b border-aurora-border flex items-center justify-between px-6 sticky top-0 z-30">

            {/* Search / Context */}
            <div className="flex items-center gap-4 flex-1">
               <div className="relative group hidden md:block">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-aurora-muted group-focus-within:text-primary transition-colors" size={18} />
                  <input
                     type="text"
                     placeholder="Search functions, history..."
                     className="bg-background-light border border-aurora-border rounded-full py-2 pl-10 pr-4 text-sm text-aurora-text focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary w-64 transition-all"
                  />
               </div>

               {/* Angle Mode Toggle */}
               <div className="flex items-center gap-1 bg-background-light border border-aurora-border rounded-lg p-1">
                  {modes.map(mode => (
                     <button
                        key={mode}
                        onClick={() => setAngleMode(mode)}
                        className={`px-3 py-1 text-xs font-bold rounded transition-all ${angleMode === mode
                           ? 'bg-primary text-white shadow'
                           : 'text-aurora-muted hover:text-aurora-text'
                           }`}
                     >
                        {mode}
                     </button>
                  ))}
               </div>
            </div>

            {/* Right Actions */}
            <div className="flex items-center gap-4">
               <button className="p-2 text-aurora-secondary hover:text-aurora-text hover:bg-white/5 rounded-full transition-colors relative">
                  <Bell size={20} />
                  <span className="absolute top-1.5 right-1.5 size-2 bg-primary rounded-full border border-background"></span>
               </button>
               <button className="p-2 text-aurora-secondary hover:text-aurora-text hover:bg-white/5 rounded-full transition-colors">
                  <Settings size={20} />
               </button>

               {/* User / Auth Section */}
               <div className="flex items-center gap-3 pl-4 border-l border-aurora-border">
                  {loading ? (
                     <div className="size-9 rounded-full bg-background-light animate-pulse" />
                  ) : user ? (
                     <>
                        <div className="text-right hidden md:block">
                           <p className="text-sm font-bold text-aurora-text leading-none truncate max-w-[120px]">
                              {user.email?.split('@')[0]}
                           </p>
                           <p className="text-[10px] text-aurora-secondary font-mono">SIGNED IN</p>
                        </div>
                        <button
                           onClick={() => signOut()}
                           className="size-9 rounded-full bg-gradient-to-tr from-primary to-secondary p-[2px] cursor-pointer hover:scale-105 transition-transform group"
                           title="Sign out"
                        >
                           <div className="size-full rounded-full bg-background-light flex items-center justify-center group-hover:bg-primary/20">
                              <LogOut size={16} className="text-primary group-hover:text-white transition-colors" />
                           </div>
                        </button>
                     </>
                  ) : (
                     <button
                        onClick={() => setShowAuthModal(true)}
                        className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-primary to-aurora-secondary rounded-full text-white font-medium text-sm hover:opacity-90 transition-opacity"
                     >
                        <LogIn size={16} />
                        <span className="hidden md:inline">Sign In</span>
                     </button>
                  )}
               </div>
            </div>
         </header>

         <AuthModal isOpen={showAuthModal} onClose={() => setShowAuthModal(false)} />
      </>
   );
};

export default TopBar;

