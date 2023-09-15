"use client";

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { useCompletion } from "ai/react";
import { ReactElement } from "react";
import { marked } from "marked";

import Spinner from "./Spinner";

export function ChatWindow(props: {
  endpoint: string,
  emptyStateComponent: ReactElement,
  placeholder?: string
}) {
  
  const { endpoint, emptyStateComponent, placeholder } = props;

  // Docs: https://sdk.vercel.ai/docs/api-reference/use-completion
  const { completion, input, stop, isLoading, handleInputChange, handleSubmit} = useCompletion({
    api: endpoint,
    onError: (e) => {
      toast(e.message, {
        theme: "dark"
      });
    },
    onFinish: () => {
      // do something with the completion result
      // toast.success('Successfully generated completion!');
    },
  });

  return (
    <div className={`flex flex-col items-center p-4 md:p-8 rounded grow overflow-hidden`}>
      {emptyStateComponent}
      <form onSubmit={handleSubmit} className="flex w-full flex-col">
        <div className="flex w-full mt-4">
          <input
            className="grow mr-8 p-4 rounded"
            value={input}
            placeholder={placeholder ?? "Enter your prompt..."}
            onChange={handleInputChange}
          />
          <button type="submit" className={`shrink-0 px-8 py-4 ${isLoading ? 'bg-slate-300' : 'bg-sky-600'} rounded w-28`} disabled={isLoading}>
            Send
          </button>
        </div>
        <div>
          <p>Response:</p>
          <div>
            {isLoading ? <Spinner /> : <span dangerouslySetInnerHTML={{__html: marked.parse(completion)}} />}
          </div>
        </div>
      </form>
      <ToastContainer/>
    </div>
  );
}
