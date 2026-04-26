import { useState, useRef, useEffect } from "react";
import { MessageSquare, X, Send, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface Msg {
  id: number;
  role: "bot" | "user";
  text: string;
}

const SUGGESTIONS = [
  "How do I scan a profile?",
  "What does the risk score mean?",
  "Safety tips for social media",
  "Report an issue",
];

const respond = (q: string): string => {
  const t = q.toLowerCase();
  if (t.includes("scan")) return "Head to the Scan page, paste a username or profile link, pick the platform, and hit ‘Start Scan’. Results appear in seconds.";
  if (t.includes("score") || t.includes("risk")) return "Risk Score ranges 0–100. 0–39 SAFE, 40–69 WARNING, 70+ DANGER. It blends followers, activity, completeness and image authenticity signals.";
  if (t.includes("tip") || t.includes("safety")) return "Top tips: never share OTPs, verify accounts before DMing, use 2FA, and run a SatyaScan on suspicious profiles before engaging.";
  if (t.includes("report") || t.includes("issue")) return "You can report a profile directly from any result page. For platform issues, email support@satyascan.ai.";
  return "I can help with scans, risk scores, safety tips, or reporting. Try one of the suggestions below!";
};

const Chatbot = () => {
  const [open, setOpen] = useState(false);
  const [msgs, setMsgs] = useState<Msg[]>([
    { id: 0, role: "bot", text: "Hey! I'm Satya, your safety assistant. How can I help today?" },
  ]);
  const [input, setInput] = useState("");
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [msgs, open]);

  const send = (text: string) => {
    if (!text.trim()) return;
    const userMsg: Msg = { id: Date.now(), role: "user", text };
    setMsgs((m) => [...m, userMsg]);
    setInput("");
    setTimeout(() => {
      setMsgs((m) => [...m, { id: Date.now() + 1, role: "bot", text: respond(text) }]);
    }, 500);
  };

  return (
    <>
      <button
        aria-label="Open assistant"
        onClick={() => setOpen((o) => !o)}
        className={cn(
          "fixed bottom-6 right-6 z-50 h-14 w-14 rounded-full bg-gradient-primary text-primary-foreground shadow-glow-primary flex items-center justify-center transition-all hover:scale-110",
          open && "scale-90 opacity-0 pointer-events-none",
        )}
      >
        <MessageSquare className="h-6 w-6" />
      </button>

      <div
        className={cn(
          "fixed bottom-6 right-6 z-50 w-[min(92vw,380px)] glass-strong rounded-2xl shadow-elegant overflow-hidden transition-all origin-bottom-right",
          open ? "scale-100 opacity-100" : "scale-90 opacity-0 pointer-events-none",
        )}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b border-border bg-gradient-to-r from-primary/10 to-transparent">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-full bg-gradient-primary flex items-center justify-center">
              <Sparkles className="h-4 w-4 text-primary-foreground" />
            </div>
            <div>
              <p className="font-semibold text-sm">Satya Assistant</p>
              <p className="text-xs text-primary flex items-center gap-1">
                <span className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" /> Online
              </p>
            </div>
          </div>
          <button onClick={() => setOpen(false)} className="p-1 rounded hover:bg-accent/20" aria-label="Close">
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="h-80 overflow-y-auto px-4 py-3 space-y-3">
          {msgs.map((m) => (
            <div key={m.id} className={cn("flex", m.role === "user" ? "justify-end" : "justify-start")}>
              <div
                className={cn(
                  "max-w-[85%] px-3 py-2 rounded-2xl text-sm animate-fade-in",
                  m.role === "user"
                    ? "bg-primary text-primary-foreground rounded-br-sm"
                    : "bg-secondary text-secondary-foreground rounded-bl-sm",
                )}
              >
                {m.text}
              </div>
            </div>
          ))}
          <div ref={endRef} />
        </div>

        <div className="px-3 pb-2 flex flex-wrap gap-1.5">
          {SUGGESTIONS.map((s) => (
            <button
              key={s}
              onClick={() => send(s)}
              className="text-xs px-2.5 py-1 rounded-full border border-border hover:border-primary hover:text-primary transition-colors"
            >
              {s}
            </button>
          ))}
        </div>

        <form
          onSubmit={(e) => {
            e.preventDefault();
            send(input);
          }}
          className="p-3 border-t border-border flex gap-2"
        >
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask anything…"
            className="flex-1 bg-input border border-border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-primary"
          />
          <Button type="submit" size="icon" variant="hero" aria-label="Send">
            <Send className="h-4 w-4" />
          </Button>
        </form>
      </div>
    </>
  );
};

export default Chatbot;
