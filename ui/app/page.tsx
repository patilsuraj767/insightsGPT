import { ChatWindow } from "@/components/ChatWindow";

export default function AgentsPage() {
  const InfoCard = (
    <div className="p-4 md:p-8 rounded bg-[#25252d] w-full max-h-[85%] overflow-hidden">
      <h1 className="text-3xl md:text-4xl mb-4">
        ▲ InsightsGPT ChatBot
      </h1>
      <h3>Using Next.js, Vercel AI SDK, Langchain, and ChromaDB under the hood. 🦜🔗</h3>
    </div>
  );
  return (
    <ChatWindow
      endpoint={process.env.API_ENDPOINT+"/query"}
      emptyStateComponent={InfoCard}
      placeholder={
        'What issue do you want me to help you resolve?'
      }
    ></ChatWindow>
  );
}
