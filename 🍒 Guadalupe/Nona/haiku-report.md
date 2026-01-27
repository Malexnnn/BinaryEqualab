# 🔧 REPORTE DE ERRORES - NONA 🍒

## ERRORES DE COMPILACIÓN

> Nona­ƒìÆ@0.1.0 build D:\PROYECTOS\Nona\Nona\Nona_DEF
> vite build

[36mvite v6.4.1 [32mbuilding for production...[36m[39m
transforming...
node.exe : 
En C:\Users\carde\AppData\Roaming\npm\pnpm.ps1: 24 Carácter: 5
+     & "node$exe"  "$basedir/node_modules/pnpm/bin/pnpm.cjs" $args
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
A PostCSS plugin did not pass the `from` option to `postcss.parse`. This may cause imported assets to be incorrectly 
transformed. If you've recently added a PostCSS plugin that raised this warning, please contact the package author to 
fix the issue.
[32mÔ£ô[39m 2208 modules transformed.
[31mÔ£ù[39m Build failed in 11.06s
[31merror during build:
[31msrc/components/auth/login-page.tsx (21:2): "AuroraSunIcon" is not exported by "src/components/cherry/index.tsx", 
imported by "src/components/auth/login-page.tsx".[31m
file: [36mD:/PROYECTOS/Nona/Nona/Nona_DEF/src/components/auth/login-page.tsx:21:2[31m
[33m
19:   CherryHStack,
20:   AuroraMusicIcon,
21:   AuroraSunIcon,
      ^
22:   AuroraSparklesIcon,
23:   AuroraZapIcon,
[31m
    at getRollupError (file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/parseAst.js:401:41)
    at error (file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/parseAst.js:397:42)
    at Module.error (file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:16956:16)
    at Module.traceVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:17412:29)
    at ModuleScope.findVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:15076:39)
    at FunctionScope.findVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:5649:38)
    at FunctionBodyScope.findVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:5649:38)
    at ReturnValueScope.findVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:5649:38)
    at FunctionBodyScope.findVariable 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:5649:38)
    at Identifier.bind 
(file:///D:/PROYECTOS/Nona/Nona/Nona_DEF/node_modules/rollup/dist/es/shared/node-entry.js:5423:40)[39m
ÔÇëELIFECYCLEÔÇë Command failed with exit code 1.


## ESTRUCTURA cherry/
- button.tsx
- card.tsx
- cherry-provider.tsx
- container.tsx
- header.tsx
- icons.tsx
- index.tsx
- input.tsx
- playground.tsx
- README.md
- simple-provider.tsx
- stack.tsx
- text.tsx


## cherry/index.tsx
```typescript
// Cherry Design System - Sistema de componentes Aurora para Nona
export { 
  CherryProvider, 
  useCherryTheme, 
  extendTheme,
  nonaTheme,
  type CherryTheme,
  type CherryProviderProps 
} from './cherry-provider';

export { 
  CherryButton,
  type CherryButtonProps 
} from './button';

export { 
  CherryInput,
  type CherryInputProps 
} from './input';

export { 
  CherryCard,
  CherryCardHeader,
  CherryCardTitle,
  CherryCardDescription,
  CherryCardContent,
  CherryCardFooter,
  type CherryCardProps 
} from './card';

export { 
  CherryText,
  CherryTitle,
  CherryHeading,
  CherrySubheading,
  CherryBody,
  CherryCaption,
  CherryLabel,
  type CherryTextProps 
} from './text';
export { CherryVStack, CherryHStack } from './stack';


import React, { HTMLAttributes, forwardRef } from 'react';
import { cn } from '../ui/utils';

export interface CherryStackProps extends HTMLAttributes<HTMLDivElement> {
  direction?: 'horizontal' | 'vertical';
  spacing?: 'none' | 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  align?: 'start' | 'center' | 'end' | 'stretch';
  justify?: 'start' | 'center' | 'end' | 'between' | 'around' | 'evenly';
  wrap?: boolean;
}

export const CherryStack = forwardRef<HTMLDivElement, CherryStackProps>(
  ({ 
    className,
    direction = 'vertical',
    spacing = 'md',
    align = 'stretch',
    justify = 'start',
    wrap = false,
    children,
    ...props 
  }, ref) => {
    
    const directionStyles = {
      horizontal: 'flex-row',
      vertical: 'flex-col',
    };

    const spacingStyles = {
      horizontal: {
        none: '',
        xs: 'gap-1',
        sm: 'gap-2',
        md: 'gap-4',
        lg: 'gap-6',
        xl: 'gap-8',
      },
      vertical: {
        none: '',
        xs: 'space-y-1',
        sm: 'space-y-2',
        md: 'space-y-4',
        lg: 'space-y-6',
        xl: 'space-y-8',
      },
    };

    const alignStyles = {
      start: 'items-start',
      center: 'items-center',

